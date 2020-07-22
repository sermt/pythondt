import pandas as pd
datos=pd.read_csv("ATP.csv")
df=pd.DataFrame(datos)
print(df)
df.reset_index().to_csv("DatosExportados.csv",header=True,index=False)
datos.set_index("Location",inplace=True)
mel=datos.loc["Melbourne"]

print(mel)
