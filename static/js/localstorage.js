const LOCAL_STORAGE_ITEMS_KEY = 'LOCAL_STORAGE_ITEMS_KEY';
const saveItemsList = () => {
    const rawItems = JSON.stringify(items);
    localStorage.setItem(LOCAL_STORAGE_ITEMS_KEY, rawItems);
}
const getSavedItems = () => JSON.parse(localStorage.getItem(LOCAL_STORAGE_ITEMS_KEY)) ?? [];
let items = getSavedItems();
const onSubmitForm = (event) => {
    event.preventDefault();
    const newData = {};
    new FormData(form).forEach((value, key) => {
        newData[key] = value;
    });
    items.push(newData);
    renderItemList(items)
    c = parseFloat(document.getElementById("Valor_Total_Insumo").value) || 0
    console.log (c)
    var z = document.getElementById("ValorT").value
    var t = document.getElementById("ValorT");
    t.value= Number(z)+Number(c)
    saveItemsList(items)
    
};

const clearLocalStorage = () => {
    items = [];
    saveItemsList();
    renderItemList([]);
} ;

renderItemList = () => {
    const list = document.querySelector('#list');
    list.innerHTML=""
    
    items.forEach((item) => {
        const newRow = `
        
            <tr>
                <td>${item.insumo}</td>
                <td>${item.cantidad}</td>
                <td>${item.valorunidad}</td>
                <td>${item.subtotal}</td>
            </tr>
        `;
        list.innerHTML += newRow;
    });
}

renderItemList(items)

const form = document.querySelector('#agregar');
form.addEventListener('submit', onSubmitForm);


const btnEliminar = document.querySelector('#borrar');
btnEliminar.addEventListener("click", clearLocalStorage)
const btnGuardar = document.querySelector('#guardar');
btnGuardar.addEventListener('click', async (event) => {
    try{
        event.preventDefault()
        const csrfmiddlewaretoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        const data = {items: items, csrfmiddlewaretoken: csrfmiddlewaretoken};
        const response = await fetch(`${new URL(window.location).origin}/CrearCompra/`, {
            method: "POST",
            redirect: 'follow', 
            body: JSON.stringify(data), headers: { "X-CSRFToken": csrfmiddlewaretoken },
        });

        console.log(window.location.origin,'holaaa')
        // if (response.status===500) throw new Error("Internal Error")
        localStorage.removeItem(LOCAL_STORAGE_ITEMS_KEY)
        items.length=0
        renderItemList(items);
        window.location = `${new URL(window.location).origin}/ListarCompra/`;
    }

    catch(error){
        
    }
    
    
});



