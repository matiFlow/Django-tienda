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

$(document).ready(function () {
    $("#productoForm input, #productoForm select").on("input", function () {
        var formIsValid = $("#productoForm")[0].checkValidity();
        $("#productoForm button[type='submit']").prop("disabled", !formIsValid);
    });
});


function limpiarBusqueda() {
    var fieldSearchName = document.getElementById("fieldSearchName");
    var fieldSearchSurname = document.getElementById("fieldSearchSurname");
    var fieldSearchDni = document.getElementById("fieldSearchDni");
    var fieldSearchTipo = document.getElementById("fieldSearchTipo");
    var fieldSearchDescripcion = document.getElementById("fieldSearchDescripcion");
    var fieldSearchPrecioMinimo = document.getElementById("fieldSearchPrecioMinimo");
    var fieldSearchPrecioMaximo = document.getElementById("fieldSearchPrecioMaximo");

    if (fieldSearchName) {
        fieldSearchName.value = "";
    }
    if (fieldSearchSurname) {
        fieldSearchSurname.value = "";
    }
    if (fieldSearchDni) {
        fieldSearchDni.value = "";
    }

    if (fieldSearchTipo) {
        fieldSearchTipo.value = "";
    }

    if (fieldSearchDescripcion) {
        fieldSearchDescripcion.value = "";
    }

    if (fieldSearchPrecioMinimo) {
        fieldSearchPrecioMinimo.value = "";
    }

    if (fieldSearchPrecioMaximo) {
        fieldSearchPrecioMaximo.value = "";
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