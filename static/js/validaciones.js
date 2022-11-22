const formulario = document.getElementById('agregar');
const inputs = document.querySelectorAll('#agregar input');

const expresiones = {
	numeroFactura: /^\d{2,6}$/, 
    cantidad: /^\d{1,6}$/, 
    valorunidad: /^\d{1,3}(\.\d{3})*(,\d+)?$/, 
    unidades: /^\d{1,6}$/,
}

const campos = {
	numeroFactura: false,
	cantidad: false,
	unidades: false,
	valorunidad: false,
}

const validarFormulario = (e) => {
	switch (e.target.name) {
		case "numeroFactura":
			validarCampo(expresiones.numeroFactura, e.target, 'numeroFactura');
		break;
		case "cantidad":
			validarCampo(expresiones.cantidad, e.target, 'cantidad');
		break;
		case "unidades":
			validarCampo(expresiones.unidades, e.target, 'unidades');
		break;
		case "valorunidad":
			validarCampo(expresiones.valorunidad, e.target, 'valorunidad');
		break;
	}
}

const validarCampo = (expresion, input, campo) => {
	if(expresion.test(input.value)){
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-correcto');
		document.querySelector(`#grupo__${campo} i`).classList.add('fa-check-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-times-circle');
		document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo');
		campos[campo] = true;
	} else {
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-correcto');
		document.querySelector(`#grupo__${campo} i`).classList.add('fa-times-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
		document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo');
		campos[campo] = false;
	}
}

inputs.forEach((input) => {
	input.addEventListener('keyup', validarFormulario);
	input.addEventListener('blur', validarFormulario);
});

