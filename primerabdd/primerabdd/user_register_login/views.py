from django.contrib.auth.views import LoginView
from django.shortcuts import render
from .forms import LoginForm


class LoginView(LoginView):
    authentication_form = LoginForm
        