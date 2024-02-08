from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        widgets = {
            'id': forms.TextInput(attrs={'required': True}),
            'nombre': forms.TextInput(attrs={'required': True}),
            'apellido': forms.TextInput(attrs={'required': True}),
            'telefono': forms.TextInput(attrs={'required': True}),
            'direccion': forms.TextInput(attrs={'required': True}),
        }