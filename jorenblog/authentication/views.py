from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from post.models import Type, Post

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = SignupForm()
        
    return render(request, 'authenticate/signup.html', {
        'form': form
    })


@login_required
def home(request):
    types = Type.objects.all()
    posts = Post.objects.all()

    return render(request, 'authenticate/home.html', {
        'types': types,
        'posts': posts
    })


def logoutuser(request):
    logout(request)
    
    return redirect('login')