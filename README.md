# Entry List extractor  
Extract name and bib from entry list PDF.   
エントリーリストのPDFから任意の選手と番号を抽出します。

## Initialization to use
Pre-condition: python 3.x is installed.  
前提条件: python3.xがインストールされていること。

1. Install pdfminer.six  
  `pip install pdfminer.six`  

1. Create member list as CSV  
  Add "Family Name, Last Name" in one line. Do not insert any spacecs. Below is the example.  
  1行に"姓,名"の形で追加してください。余分な空白が入ると抽出に失敗します。以下にMemberList.csvの例を示します。
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
Use member list prepared at #2 and entry list PDF each organizer published.  
2で準備したメンバーリストと各レース主催者が公開するエントリーリストのPDFを使用してください。

## Note
PDFMiner is currently the best tool for analyzing Japanese PDFs. Contributions from those with expertise in PDF or Python are welcome.  
現時点でPDFMinerが日本語を含むPDFの解析に最も優れていると考えられます。本ツールへの変更はWelcomeです。
