import tabula

path = 'test.pdf'

df = tabula.read_pdf(path, encoding='gbk', pages='all')
for indexs in df.index:
    print(df.loc[indexs].values)

# tabula.convert_into(path, os.path.splitext(path)[0]+'.csv', pages='all')