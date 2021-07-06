from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Productos


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {k: "" for k in fields}


class FormProducto(forms.ModelForm):
    # titulo = forms.CharField(label='Titulo', widget=forms.TextInput)

    # campos del modelo
    class Meta:
        model = Productos
        fields = ('titulo', 'categoria', 'image', 'contenido', 'precio',
                  )
        widgets = {
            'precio': forms.NumberInput(attrs={'class': 'precio'}),
            'categoria': forms.Select(attrs={'class': 'categoria'}),
            'titulo': forms.TextInput(attrs={'class': 'titulo'}),
            'contenido': forms.Textarea(attrs={'class': 'contenido'}),
            'image': forms.FileInput(attrs={'name': 'imagen_adjunta', 'class': 'image'}),
        }
