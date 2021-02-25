let persona={
nombre: "Juan",
apellido: "Perez",
edad: 18,
telefono: 31315465465,
idioma: "MX",
// get otorga el nombre a la funcion
get nombreCompleto(){
	return this.nombre+ ' ' + this.apellido;
},
get lang(){
	return this.idioma.toUpperCase();
},
set lang(lang){
	this.idioma=lang.toUpperCase();
}
}
console.log(persona.nombreCompleto);

// metodo alternativo

let persona2 = new Object();
persona2.nombre = "Miguel";
persona2.apellido= "Martinez";

console.log(persona2.nombre);
for (propiedad in persona){
	console.log(propiedad);
	console.log(persona[propiedad]);
}
//eliminar una propiedad

persona.lang='en';
delete persona.telefono;
console.log(persona);
//mas maneras de imprimir un objeto
let personaObj= Object.values(persona);
console.log(personaObj);
let personaString = JSON.stringify(persona);
console.log(personaString);

//funcion constructor de objetos de tipo persona
function Persona(nombre,edad,telefono){
this.nombre = nombre;
this.apellido = 'Perez';
this.edad = edad;
this.telefono=telefono;
this.nombreCompleto = nombre + ' ' + this.apellido;
this.nombre2 = function(){
	return this.edad + this.telefono
}
}

let Persona1= new Persona('Juan',20,54645);
console.log(Persona1)
//la propiedad prototype agrega ese mismo valor a todos los objetos de la misma clase
// Persona.prototype.tel = 4564654554 -- agregaria ese valor a todos los objetos persona