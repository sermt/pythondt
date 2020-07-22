import pandas as pd 

#import matplotlib.pyplot as plt
datos = pd.read_csv('precios.csv',header=0)
df=pd.DataFrame(datos)
print(df,'\n')
TK=df['precio']+273.15
df=df.assign(kelvin=TK.values)
print(df)

df.to_csv('modEnergy.csv',sep='\t')