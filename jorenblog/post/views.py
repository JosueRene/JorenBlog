from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Post

from .forms import CreatePostForm

# Create your views here.
def hello(request):
    return HttpResponse("hello page")


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

    form = CreatePostForm()

    return render(request, 'post/new.html', {
        'form': form,
        'title': 'New Post'
    })