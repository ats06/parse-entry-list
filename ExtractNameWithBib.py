""" 
  This script extracs names listed in member list from entry list PDF file.
  (Tested with entry lists Mt.FUJI, OSJ and Okushinano)

  Before using script, please install pdfminer.
  % pip install pdfminer.six
"""
import csv
import re
import sys

import logging

from io import StringIO
from pdfminer.high_level import extract_text_to_fp

# Read PDF as plane text
def extract_text_from_pdf(pdf_path):
    fp_out = StringIO()
    with open(pdf_path, 'rb') as fp_in:
        extract_text_to_fp(fp_in, fp_out)
        # Replace code from Newpage(0x0c) to Newline(0x0a)
        # It seems that a page is extracted as consists of one line and Newpage character
        text = fp_out.getvalue()
        return text.replace(chr(12), chr(10))

# Read member list as matrix
# [['山田','太郎'],['トレイル','ランガ'], ...]
def extract_member_from_list(list_path):
    with open(list_path, encoding='utf8', newline='') as f:
        reader = csv.reader(f)
        return [row for row in reader]

### Main
args = sys.argv
if len(args) != 3:
    print('Usage: python ExtractNameWithBib.py [member.csv] [input.pdf]')
    exit()

# Don't show warning message "CropBox missing from /Page, defaulting to MediaBox".
logging.getLogger('pdfminer').setLevel(logging.ERROR)

member_list_fname = args[1]
entry_list_fname = args[2]

text = extract_text_from_pdf(entry_list_fname)
members = extract_member_from_list(member_list_fname)

print('===== %s =====' % entry_list_fname)
for member in members:
    # Find string "Family name + Zenkaku/Hankaku/Tab space + Last name".
    # Family name: row[0], Last name: row[1]
    pattern = member[0] + '[\\s\\u3000\\t]*' + member[1]
    m = re.search(pattern, text)

    if m != None:
        name = m.group().replace('\u3000', ' ')
        # Assume that bib number is in front of name within eight character.
        # Show the nearest one to name as bib number in case multiple figures found.
        bib = re.findall(r'\d+', text[m.start()-4:m.start()])
        bib_number = bib[-1] if bib else ''

        print('{:<5} {}'.format(bib_number, name))
