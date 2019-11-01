from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.contrib import messages
from django.shortcuts import redirect
from crm.models import Organizacion




class LoginView(LoginView):
    authentication_form = LoginForm

        

def login_success(request):
    organizacion = Organizacion.objects.filter(usuario=request.user)[:1].get()
    
    if organizacion.tyc_leido:
        return redirect("home")
    else:
        messages.error(request,'TyC')
        organizacion.tyc_leido = True
        organizacion.save()
        return redirect("home")