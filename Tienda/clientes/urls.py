from django.urls import path
from .views import *
from . import views

app_name = 'cliente_app' 

urlpatterns = [
    path(
        'listadoClientes/',
        views.ClienteListar.as_view(),
        name='listado_clientes'
    ),
    path(
        'crearCliente/',
        views.ClienteCrear.as_view(),
        name='crear_cliente'
    ),
    path(
        'editarCliente/<pk>/',
        views.ClienteEditar.as_view(),
        name='editar_cliente'
    ),
    path(
        'borrarCliente/<pk>/',
        views.ClienteBorrar.as_view(),
        name='borrar_cliente'
    )
]