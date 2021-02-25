class Producto{
	// las variables static solo se asocian con la clase y no con los objetos	
	static contadorProducto=0;
	constructor(nombre,precio){
		this._idProducto = ++Producto.contadorProducto;
		this._nombre= nombre.toUpperCase();
		this._precio=precio;

	}
	get idProducto(){
		return this._idProducto;
	}

	get Nombre(){
		return this._nombre;
	}


		get Precio(){
		return this._precio;
	}
	toString(){
		return `idProducto: ${this._idProducto}, Nombre: ${this._nombre}, Precio: ${this._precio} `
	}
}

let producto1= new Producto('Pantalon', 200);
let producto2 = new Producto('Camisa', 150);
producto2._precio=180;
console.log(producto1.toString());
console.log(producto2.toString());