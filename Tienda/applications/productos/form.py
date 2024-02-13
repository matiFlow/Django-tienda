from django import forms
from .models import Producto
from .models import Marca

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'id': forms.TextInput(attrs={'required': True}),
            'tipo': forms.TextInput(attrs={'required': True}),
            'descripcion': forms.TextInput(attrs={'required': True}),
            'precio': forms.TextInput(attrs={'required': True}),
            'cantidad': forms.TextInput(attrs={'required': True}),
            'marca': forms.SelectMultiple(attrs={'required': True}),
            'proveedor': forms.Select(attrs={'required': True}),
        }

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'
        widgets = {
            'idMarca': forms.TextInput(attrs={'required': True}),
            'marca': forms.TextInput(attrs={'required': True})
        }