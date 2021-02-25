/* Ejemplos de tipos de datos en JavaScript*/

//Tipo String

var nombre= "Juan";
console.log(typeof nombre);

//Tipo numerico
var num= 123123123;
// typeof , devuelve el tipo que almacena una variable
console.log(typeof num);

//Tipo objeto
var ob= {
	nombre: "Juan",
	apellido:"Perez",
	edad: "18",
	telefono: "1234567890"
}
console.log(ob.nombre)

//tipo booleana

var bandera= true;
console.log(typeof bandera)


// funcion
function miFuncion(){}
console.log(typeof miFuncion);

//tipo symbol

var simbolo= Symbol("mi simbolo");
console.log(typeof simbolo);

//tipo clase
class Personal{
	constructror(nombre, apellido){
		this.nombre=nombre;
		this.apellido=apellido;
	}
}
console.log(typeof Personal);

//tipo unndefined

var x;
console.log(x);
//tipe null
var y = null;
console.log(typeof y);

//arreglo

var autos=["uno","dos","tres"];
console.log(autos)
//cadena vacia
var z= '';
console.log(z);