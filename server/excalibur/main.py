import camelot

# ref: https://camelot-py.readthedocs.io/en/master/index.html
tables = camelot.read_pdf('MIL-STD-6016G_page_516.pdf')
tables.export('MIL-STD-6016G_page_516.csv', f='csv', compress=True)