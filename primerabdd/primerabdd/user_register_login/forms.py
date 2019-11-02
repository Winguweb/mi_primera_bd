from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class LoginForm(AuthenticationForm):
    
    username = UsernameField(label='Usuario de la organización', widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Usuario'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}), label='Contraseña')
