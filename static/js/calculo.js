function calcular(){
    try {
        var a = parseFloat(document.getElementById("unidades").value) || 0,
         b = parseFloat(document.getElementById("valorunidad").value) || 0;

        document.getElementById("Subtotal").value = a * b;
    } catch(e){}
}

const Cantidad = document.querySelector("#Cantidad")
    const Valor_Unitario = document.querySelector("#Valor_Unitario")
    const Valor_Total_Insumo = document.querySelector("#Valor_Total_Insumo")
    const Valor_Total = document.querySelector("#ValorT")

    const CalcularT = () => {
        Valor_Total_Insumo.value =(Valor_Unitario.value * Cantidad.value).toLocaleString("en",{
            style: "currency",
	        currency: "COP"
        });
        Valor_Total.value = Valor_Total_Insumo.value
        Valor_Total.value = (Valor_Total_Insumo + Valor_Total)
        
    }
    let search_date = document.getElementById("search_date");

    search_date.max = today;