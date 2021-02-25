function miFuncion(a,b){
//console.log( "La suma de a y b es " + (a+b));
//console.log(arguments.length); imprime la cantidad de argumentos
// arguments[0];
// let valor=arguments[1];
// console.log(valor); los argumentos pueden llegar a ser mas que los parametros
return a+b;
}
//Lmmado de la funcion
let resultado = miFuncion(2,2);
console.log(" El resultado es: "+resultado);
//declaracion de funcion de tipo expresion
let x = function (a,b){ return a+b};
resultado = x(1,2);
console.log(" El resultado es: "+resultado);

//self invoking
(function (){
	console.log("Funcion automatica");
})();
//Convertir funcion a cadena o texto
//let texto= miFuncion.toString();
//console.log(texto);

//funciones tipo flecha
let funcionFlecha= (a,b) => a+b;
console.log(funcionFlecha(5,6))
// paso por referencia

const persona= {
	nombre: "Aleman",
	apellido: "Valdez"

}
function cambiar(p){
p.nombre = "Jin";
}
cambiar(persona);
console.log(persona.nombre);