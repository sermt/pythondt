//let arreglo=new Array[ "uno", "dos", "tres"];

const arreglo=[ "uno", "dos", "tres"];

//recorrer un arreglo
for (var i = 0; i <= arreglo.length-1; i++) {
	console.log(arreglo[i])
}


//modificar un arreglo con base en su indice

arreglo[0]= "Diez";
console.log(arreglo[0])
arreglo.push("Once");// metodo push
console.log(arreglo);

arreglo[arreglo.length]= "Doce";
console.log(arreglo);
arreglo[arreglo.length]= "Doce";
console.log(arreglo);
//Saber si es un arreglo
console.log(Array.isArray(arreglo));
console.log(arreglo instanceof Array);