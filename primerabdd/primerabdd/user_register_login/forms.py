from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField#, PasswordInput

class LoginForm(AuthenticationForm):
    
    username = UsernameField(label='Usuario de la organización', widget=forms.TextInput(attrs={'autofocus': True}))

    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')