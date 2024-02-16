from django.contrib import admin
from django.urls import path
from . import views

app_name = 'inicio_app'

urlpatterns = [
    path(
        '',
        views.Inicio.as_view(),
        name='inicio'
    ),
    path(
        'login',
        views.LoginUser.as_view(),
        name='login-user'
    ),
    path(
        'logout',
        views.LogoutView.as_view(),
        name='logout-user'
    )
]