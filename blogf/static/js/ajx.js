$(document).ready(function(){
	//alert("holas");
	$("button.pop").click(function (event){
		event.preventDefault();
		//alert("holas");
		var ass=event.target.id;
		var as=ass.split(",");
		var id=as[1];
		//alert(id);
		 $.ajax({
            type: 'POST',
            url: "ajax_madurar",
            data: {"id":id},
            success: function (success) {

             swal({
 				title: 'Exito!',
  				text: success,
  				confirmButtonText: 'Continuar'
						})
            },
            error: function () {
                alert("Problemas en la red, volver a intentar mas tarde")
            }
        });
	});
	});
