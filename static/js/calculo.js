function calcular(){
    try {
        var a = parseFloat(document.getElementById("unidades").value) || 0,
         b = parseFloat(document.getElementById("valorunidad").value) || 0;

        document.getElementById("Subtotal").value = a * b;
    } catch(e){}
}