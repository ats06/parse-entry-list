# Entry List extractor  
Extract name and bib from entry list.   
エントリーリストから任意の選手のエントリー情報を抽出します。  

## Initialization to use
1. Install pdfminer  
  `pip install pdfminer`

1. Create member list as CSV
  CSV should be consisted as below.
  ```
  山田,太郎
  トレイル,ランガ
  ```

## Executin
`python ExtractNameWithBib.py [EntryList.pdf]`

## Note
PDFMiner is currently the best tool for analyzing Japanese PDFs. Contributions from those with expertise in PDF or Python are welcome.