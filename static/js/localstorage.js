const LOCAL_STORAGE_ITEMS_KEY = 'LOCAL_STORAGE_ITEMS_KEY';
const saveItemsList = () => {
    const rawItems = JSON.stringify(items);
    localStorage.setItem(LOCAL_STORAGE_ITEMS_KEY, rawItems);
}
const getSavedItems = () => JSON.parse(localStorage.getItem(LOCAL_STORAGE_ITEMS_KEY)) ?? [];
const items = getSavedItems();
const onSubmitForm = (event) => {
    event.preventDefault();
    const newData = {};
    new FormData(form).forEach((value, key) => {
        newData[key] = value;
    });
    items.push(newData);
    renderItemList()
    saveItemsList()
};

renderItemList = () => {
    const list = document.querySelector('#list');
    list.innerHTML=""
    
    items.forEach((item) => {
        const newRow = `
<<<<<<< HEAD
=======
        
>>>>>>> Julian
        <thead>
            <tr>
                <th>Nombre</th>
                <th>Cantidad</th>
                <th>Precio</th>
                <th>Total</th>
            </tr>
<<<<<<< HEAD
         </thead>
=======
        </thead>
>>>>>>> Julian
            <tr>
                <td>${item.insumo}</td>
                <td>${item.cantidad}</td>
                <td>${item.valorunidad}</td>
                <td>${item.ValorTotalInsumo}</td>
            </tr>
        `;
        list.innerHTML += newRow;
    });
}

renderItemList()

const form = document.querySelector('#agregar');
form.addEventListener('submit', onSubmitForm);



const btnGuardar = document.querySelector('#guardar');
btnGuardar.addEventListener('click', async () => {
    try{
        const csrfmiddlewaretoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        const data = {items: items, csrfmiddlewaretoken: csrfmiddlewaretoken};
        const response = await fetch(`${new URL(window.location).origin}/CrearCompra/`, {
            method: "POST",
            redirect: 'follow', 
            body: JSON.stringify(data), headers: { "X-CSRFToken": csrfmiddlewaretoken },
        });
        // if (response.status===500) throw new Error("Internal Error")
        localStorage.removeItem(LOCAL_STORAGE_ITEMS_KEY)
        items.length=0
        renderItemList();
    }

    catch(error){
        
    }
    
    
});

