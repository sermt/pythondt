let numero= "10";

let realNumero = Number(numero);

let cadena= "hola";

let ternario = (realNumero<18) ? "Menor de edad" : "Mayor de edad";
console.log(ternario);
// funcion que retorna si es o no un numero la variable que se revisa
if (isNaN(realNumero)){ console.log("No es un numero");} else {console.log("Es un numero");}