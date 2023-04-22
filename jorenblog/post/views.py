from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post

# Create your views here.
def hello(request):
    return HttpResponse("hello page")


def detail(request, pk):
    post = get_object_or_404(Post, pk = pk)

    return render(request, 'post/detail.html', {
        'post': post
    })
