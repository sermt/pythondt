import pandas as pd 

#import matplotlib.pyplot as plt
datos = pd.read_csv('precios.csv')
df=pd.DataFrame(datos)
def monto(a,b):
	costo=a*b
	return costo

producto=input(' Introduce tu producto ')
piezas=int(input(" ¿Cuántas piezas necesitas? "))
precio=df[df['producto']==producto]['precio']
print(precio)
total=monto(piezas,precio)
print("El total a pagar es: ", total)