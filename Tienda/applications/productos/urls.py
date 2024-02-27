from django.urls import path
from .views import *
from . import views

app_name = 'producto_app' 

urlpatterns = [
    path(
        'listadoProductos/',
        views.ProductoListar.as_view(),
        name='listado_productos'
    ),
    path(
        'crearProducto/',
        views.ProductoCrear.as_view(),
        name='crear_producto'
    ),
    path(
        'detalleProducto/<pk>/',
        views.ProductoDetalles.as_view(),
        name='detalle_producto',
    ),
    path(
        'borrarProducto/<pk>/',
        views.ProductoBorrar.as_view(),
        name='borrar_producto'
    ),
    path(
        'editarProducto/<pk>',
        views.ProductoEditar.as_view(),
        name='editar_producto'
    ),
    path(
        'crearMarca/',
        views.MarcaCrear.as_view(),
        name='crear_marca'
    ),
    path(
        'listadoProductos/api/',
        views.ProductoListApiView.as_view(),
        name='listado_productos_api'
    )
]