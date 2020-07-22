import pandas as pd
datos=pd.read_csv("ATP.csv")
df=pd.DataFrame(datos)
datos.set_index("Location", inplace=True)
print(datos)
print('\n')
print(datos.loc[:,"ATP"])#obtener toda una columna 
print("\n")
print(datos.loc[datos["Court"]=="Outdoor",["Surface"]])#condicion, lo que quieres que se muestre
#mas de una condicion
print("\n")
print(datos.loc[datos['Series'].str.endswith('Slam')&(datos['Surface']=="Clay")&(datos['Winner']=="Federer R.")&(datos['Round']=='The Final')])