from django.contrib.auth import authenticate
from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'dni': forms.TextInput(attrs={'required': True}),
            'nombre': forms.TextInput(attrs={'required': True}),
            'apellido': forms.TextInput(attrs={'required': True}),
            'telefono': forms.TextInput(attrs={'required': True}),
            'direccion': forms.TextInput(attrs={'required': True}),
        }
