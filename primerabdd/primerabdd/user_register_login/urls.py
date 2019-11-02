from django.urls import path, include
from . import views

urlpatterns = [
 	path('login/', views.LoginView.as_view(template_name='registration/login.html', redirect_authenticated_user=True), name='login'),
 	path('login_success/', views.login_success, name='login_success')

]