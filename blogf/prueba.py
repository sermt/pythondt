from PIL import Image
import pymongo
import base64

my_client = pymongo.MongoClient("mongodb+srv://admin:bananospunta@bananos.c9fhp.mongodb.net/bananos?retryWrites=true&w=majority")
my_db=my_client['bananosDB']
col_bana= my_db['bananos']

def busid():
	totales=[]
	X= col_bana.find({'Estado':'Madurando'}).count()
	for x in col_bana.find({'Estado':'Madurando'}):
		img=x['Imagen']
		image_64_decode = base64.decodebytes(img) 
		image_result = open("static/img/{}img.jpg".format(x['_id']), 'wb') # create a writable image and write the decoding result
		image_result.write(image_64_decode)
		x.pop('Imagen')
		totales.append(x)
	#print(totales)
	return totales,X
#busid()
#banano1---{"id":1,'Dispositivo': 1, 'Fecha/Hora': {2,2,2,2,2,2,2,2,2},}
def cambiar(id):
	try:
		ad=(int(id))
		for x in col_bana.find({'Estado':'Madurando'}):
					myquery = { "_id": ad }
					newvalues = { "$set":  {  'Estado': 'Procesado'} } 
					col_bana.update(myquery, newvalues)
		return 'Cambio efectuado correctamente'
	except Exception as e:
		return print(e)
