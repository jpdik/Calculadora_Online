$(document).ready(function(){

	var ligada = true;

	$( ".btn" ).click(function() {
		comando = $(this).text().charCodeAt(0);
		
		if(comando == 61){
			if(ligada == true)
				Calcular();
		}
		else if(comando == 67){
			if(ligada == true)
				Apagar_Visor();
		}
		else if($(this).text() == 'ON'){
			Interruptor(true);
		}
		else if($(this).text() == 'OFF'){
			Interruptor(false);
		}
		else{
			if(ligada == true)
  				Inserir_Valor($(this).text());
  		}
	});

	function Interruptor(valor){
		if(valor == true){
			$('#visor').css({backgroundColor: "white" });
		}
		else{
			$('#visor').css({backgroundColor: "black" });
			Apagar_Visor();
		}


		ligada = valor
	}

	function Inserir_Valor(valor){
		if(valor == "+" || valor == "-" || valor == "*" || valor == "/" || valor == "%")
			$('#visor').val($('#visor').val() + " " + valor + " ");
		else
			$('#visor').val($('#visor').val() + valor);
	}

	function Apagar_Visor(){
		$('#visor').val("");
	}

	function Calcular(){
		var jsonAsString = JSON.stringify({ valores: $('#visor').val().split(" ")});

		$.ajax({
			url: window.location.href+'calcular',
				success: function (e) {
				    var resp = JSON.parse(JSON.stringify(e));
					$('#visor').val(resp['resposta'])
				},
				error: function (e) {
					alert(e)
				},
			type: 'POST',
		    data: jsonAsString,
		    contentType: 'application/json',
		    dataType: 'json'
		});
	}

	//Analise de tecla pressionada dentro do body(corpo da página) para realizar os comandos.
	document.querySelector('body').addEventListener('keyup', function(event) {
 
		var tecla = event.key;
		var key = event.keyCode;

		if(tecla >= 0 || tecla <= 9 || tecla == "+" || tecla == "-" || tecla == "*" || tecla == "/" || tecla == "%") {
			Inserir_Valor(tecla);
		}
		else if(key == 8){
			Apagar_Visor();
		}
		else if(key == 13){
			Calcular();
		}
	});
});
