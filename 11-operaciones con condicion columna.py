import pandas as pd 
datos=pd.read_csv("minutos2.csv")
df=pd.DataFrame(datos)
print(df)
alto=df.loc[0,'B']
df["pB"]=df["B"].diff(1)
for i in range(1,len(df)):
	if df.loc[i,"B"]>df.loc[i-1,"B"] and df.loc[i,"B"]>alto:
			df.loc[i,"dB"]=df.loc[i,"B"]-alto
			alto=df.loc[i,"B"]
	else:
		df.loc[i,"dB"]=0
print(df)
total=df["dB"].sum()
print("El total es: ", total)
print("La suma parcial es: ", df.loc[datos["pB"]>0, "pB"].sum())
df.reset_index().to_csv("minutos2.csv",header=True, index=False)


