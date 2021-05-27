from django.shortcuts import render
from django.http import HttpResponse\

from .models import Post


def index(request):
    posts = Post.objects.all().order_by("-id")[:3]
    return render(request, 'index.html', {'posts': posts})

def post_list(request):

    posts = Post.objects.all()
    return render(request, 'blog/blog-list.html', {'posts': posts})


def post_detail(request, id):

    post = Post.objects.get(id=id)
    return render(request, 'blog/blog-detail.html', {'post': post})
