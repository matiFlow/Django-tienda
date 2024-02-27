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

class LoginForm(forms.Form):
    username = forms.CharField(
        label = 'Usuario',
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'usuario',
                'class' : 'form-control',
                'type' : 'text',
            }
        )
    )
    password = forms.CharField(
        label = 'Contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'contraseña',
                'class' : 'form-control',
                'type' : 'password',
            }
        )
    )
    

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Los datos ingresados son incorrectos")

        return self.cleaned_data