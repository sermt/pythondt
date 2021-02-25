let persona={
	nombre: 'Juan',
	apellido: 'Anotny',
	nombreCompleto: function(titulo,tel){
		return titulo+ ':'+this.nombre + ' '+ this.apellido+ 'telefono: '+tel
	}
}
let persona2={
	nombre: 'raiz',
	apellido: 'rezpe'
}
//uso de call
//el metodo persona1.nombreCompleto() con los datos de persona2
console.log(persona.nombreCompleto.call(persona2, 'ing.', 46546578));
let arreglo=['ing.', 566456454]
//metodo apply
console.log(persona.nombreCompleto.apply(persona2, arreglo));