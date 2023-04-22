from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs= {
        'placeholder': 'Enter your username',
        'class': 'form-control mb-4 mt-5'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password',
        'class': 'form-control mb-5'
    }))
    

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs= {
        'placeholder': 'Enter your username',
        'class': 'form-control mb-4 mt-5'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email',
        'class': 'form-control mb-5'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your password',
        'class': 'form-control mb-5'
    }))
 
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 're-type password',
        'class': 'form-control mb-5'
    }))