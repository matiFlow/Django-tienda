from django.contrib import admin
from django.urls import path
from . import views

app_name = 'inicio_app'

urlpatterns = [
                path(
                    '',
                    views.Inicio.as_view(),
                    name='inicio'
                )
]