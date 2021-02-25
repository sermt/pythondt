let a=1,b=2,c;
let s="tres";
c=a*b;
//las expresiones se evaluan de izq a der pero hay prioridades con los operadores *>+
console.log(c);

// operadores de asignacion
a += 4; // a=a+4
a-=2;//a=a-2
//resto de operadores *=,/=,%=...
// == devuelve falso/verdadero al comparar la igualdad      //      ===  	se revisa el valor sin importar el tipo
// =1    revisa el valor sin importar el tipo           //      !==     se revisa el valor y el tipo
// operadores relacionales <,>,=>,=>
let i = a==b;
let o= a===s;
console.log(i,o);

//console.log(a);
//operador ternario
let resultado = (3>2)? "verdadero" : "Falso";
console.log(resultado);