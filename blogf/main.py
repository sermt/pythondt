from flask import Flask
from flask import request
from flask import render_template
from prueba import * 

app=Flask(__name__)
#template_folder='pruebas' esto en caso de que se utilize una carpeta que no se llame templates
#http://localhost:8000/params?params1=Hola_mundo&params2=otravez
totales,cuenta=busid()
vls=[]
litms=[]
lval=[]
#print(cuenta)
if (cuenta>0):
	for x in range(cuenta):
		# titulo=totales[x].keys()
		val=list(totales[x].values())
		itms=totales[x].items()
		#print(totales[x]['_id'])
		# ltitulo.append(titulo)
		lval.append(val[0])
		litms.append(itms)
		vls.append(str(totales[x]['_id']))

		# for x,y in litms[0]:
		# 	print(y)
	#print(lval,lval[0])
@app.route('/')
def inicio():
	return render_template('index.html')
@app.route('/Monitoreo')
def monitoreo():
	return render_template('monitoreo.html',t1=litms,cuenta=cuenta,asd=vls,vals=lval)

@app.route('/ajax_madurar', methods=['POST'])

def madurar():
	id=request.form['id']
	return cambiar(id)
if (__name__ == '__main__'):
	app.run(debug=True,port=8000)