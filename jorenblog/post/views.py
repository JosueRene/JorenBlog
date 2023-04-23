from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Post

from .forms import CreatePostForm, EditPostForm

# Create your views here.
def detail(request, pk):
    post = get_object_or_404(Post, pk = pk)

    return render(request, 'post/detail.html', {
        'post': post
    })


@login_required
def newpost(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.save()

            return redirect('post:dashboard')
    else:
        form = CreatePostForm()

    return render(request, 'post/new.html', {
        'form': form,
        'title': 'New Post'
    })



@login_required
def editpost(request, pk):
    post = get_object_or_404(Post, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditPostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()

            return redirect('post:dashboard')
    else:
        form = EditPostForm(instance=post)

    return render(request, 'post/new.html', {
        'form': form,
        'title': 'New Post'
    })



@login_required
def dashboard(request):
    posts = Post.objects.filter(created_by=request.user)

    return render(request, 'post/dashboard.html', {
        'posts': posts
    })


@login_required
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk, created_by=request.user)
    post.delete()

    return redirect('post:dashboard')
