from django.urls import path
from .views import *
from . import views

app_name = 'proveedor_app' 

urlpatterns = [
    path(
        'listadoProveedores/',
        views.ProveedorListar.as_view(),
        name='listado_proveedores'
    ),
    path(
        'crearProveedor/',
        views.ProveedorCrear.as_view(),
        name='crear_proveedor'
    ),
    path(
        'editarProveedor/<pk>/',
        views.ProveedorEditar.as_view(),
        name='editar_proveedor'
    ),
    path(
        'borrarProveedor/<pk>/',
        views.ProveedorBorrar.as_view(),
        name='borrar_proveedor'
    )
]