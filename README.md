# Entry List extractor  
Extract name and bib from entry list.   
エントリーリストから任意の選手のエントリー情報を抽出します。  

## Initialization to use
1. Install pdfminer.six  
  `pip install pdfminer.six`

1. Create member list as CSV  
  Add "Family Name, Last Name" in one line. Do not insert any spacecs. Below is the example 
  ```
  山田,太郎
  桜木,花道
  孫,悟空
  トレイル,ラン
  山,渓谷
  ワンダー,フォーゲル
  ```

## Executin
`python ExtractNameWithBib.py [MemberList.csv] [EntryList.pdf]`

## Note
PDFMiner is currently the best tool for analyzing Japanese PDFs. Contributions from those with expertise in PDF or Python are welcome.
