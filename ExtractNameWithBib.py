""" 
  This script extracs names listed in member list from entry list PDF file.
  (Tested with entry lists Mt.FUJI, OSJ and Okushinano)

  Before using script, please install pdfminer.
  % pip install pdfminer.six
"""
import csv
import re
import sys

from io import StringIO
from pdfminer.high_level import extract_text_to_fp
from pathlib import Path

args = sys.argv
if len(args) != 3:
    print('Usage: python ExtractNameWithBib.py [member.csv] [input.pdf]')
    exit()

member_list_fname = args[1]
entry_list_fname = args[2]
#member_list_fname = 'member_list.csv'  # Todo: Get file from args

# Read PDF into buffer
fp_out = StringIO()
with open(Path(entry_list_fname), 'rb') as fp_in:
    extract_text_to_fp(fp_in, fp_out)

# Replace code from Newpage(0x0c) to Newline(0x0a)
# It seems that a page is extracted as consists of one line and Newpage character
text = fp_out.getvalue()
text = text.replace(chr(12), chr(10))  
#print(text)

print('===== Entries =====')

with open(member_list_fname, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        # Find string "Family name + Zenkaku/Hankaku/Tab space + Last name".
        # Family name: row[0], Last name: row[1]
        pattern = row[0] + '[\\u3000 \\t]' + row[1]   # FixMe: 甲州アルプスで姓名の間の全角スペースが検出できない
        #pattern = row[0] + '(?:\s|　\\t)?' + row[1]  # WA for Koshu Alps 
        m = re.search(pattern, text)
        if m != None:
            
            name = m.group().replace('\u3000', ' ')
            # Assume that bib number is in front of name within eight character.
            # Show the nearest one to name as bib number in case multiple figures found.
            bib = re.findall(r'\d+', text[m.start()-4:m.start()])
            if len(bib) != 0:
                print(f'{bib[len(bib)-1]} {name}')
            else:
                print(f'{name}')
            
