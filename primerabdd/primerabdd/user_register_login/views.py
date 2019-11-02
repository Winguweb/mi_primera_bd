from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.contrib import messages
from django.shortcuts import redirect
from crm.models import Organizacion
import sweetify
import os




class LoginView(LoginView):
    authentication_form = LoginForm

        

def login_success(request):
    organizacion = Organizacion.objects.filter(usuario=request.user)[:1].get()
    
    if organizacion.tyc_leido:
        return redirect("home")
    else:
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, 'tyc/tyc.txt')
        
        with open(file_path, 'r') as file:
            tyc = file.read()
            sweetify.info(request, 'Términos y Condiciones', text=tyc, persistent='Estoy de acuerdo!')
            organizacion.tyc_leido = True
            organizacion.save()
            return redirect("home")