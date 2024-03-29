from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm

urlpatterns = [
    path('', views.signup, name='signup' ),
    path('login/', auth_views.LoginView.as_view(template_name= 'authenticate/login.html', authentication_form=LoginForm) , name='login' ),
    path('home/', views.home, name='home'),
    path('logout/', views.logoutuser, name='logout')
]