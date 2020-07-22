import pandas as pd 
archivo=pd.ExcelFile("estadosmx.xlsx")
print(archivo.sheet_names)
df=archivo.parse('estadosmx')
print(df)
