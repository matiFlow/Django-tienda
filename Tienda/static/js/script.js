$(document).ready(function () {
    $("#clienteForm input, #clienteForm select").on("input", function () {
        var formIsValid = $("#clienteForm")[0].checkValidity();
        $("#clienteForm button[type='submit']").prop("disabled", !formIsValid);
    });
});

$(document).ready(function () {
    $("#proveedorForm input, #proveedorForm select").on("input", function () {
        var formIsValid = $("#proveedorForm")[0].checkValidity();
        $("#proveedorForm button[type='submit']").prop("disabled", !formIsValid);
    });
});


function limpiarBusqueda() {
    var fieldSearchName = document.getElementById("fieldSearchName");
    var fieldSearchSurname = document.getElementById("fieldSearchSurname");
    var fieldSearchDni = document.getElementById("fieldSearchDni");

    if (fieldSearchName) {
        fieldSearchName.value = "";
    }
    if (fieldSearchSurname) {
        fieldSearchSurname.value = "";
    }
    if (fieldSearchDni) {
        fieldSearchDni.value = "";
    }
    history.replaceState({}, document.title, removeSearchParamsFromURL(window.location.href));

    document.getElementById("formSearch").submit();

    return false; 
}

function removeSearchParamsFromURL(url) {
    return url.split("?")[0];
}

function eliminarRegistro(id){
    console.log(id)

    return false
}