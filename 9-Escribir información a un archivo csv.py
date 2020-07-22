dic={"Aguascalientes":"Aguascalientes", "Sonora":"Hermosillo", "Nayarit":"Tepic"}
archivo="estadosmx.csv"
csv=open(archivo,"w")
titulo="Estado"+','+"Capital\n"
csv.write(titulo)
for k in dic.keys():
	estado=k
	capital=dic[k]
	fila=estado+","+capital+"\n"
	csv.write(fila)