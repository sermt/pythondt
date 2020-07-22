import pandas as pd 
import numpy as np
datos=pd.read_csv("DatosYT.csv")
print(datos.dtypes)
#ordenar valor por id ascending
print(datos.sort_values(by=['id'],ascending=[False]))
#
df1=pd.DataFrame(np.sort(datos.values, axis=0), index=datos.index, columns=datos.columns)
print(df1)