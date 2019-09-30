from django.contrib.auth.views import LoginView
from .forms import LoginForm


class LoginView(LoginView):
    authentication_form = LoginForm

        