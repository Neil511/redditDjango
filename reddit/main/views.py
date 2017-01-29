from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def data(request):
    posts = Post.objects.all()
    return render(request, 'data.html', {'posts': posts})

def posts(request, post_id):
    post = Post.objects.get(id = post_id)
    return render(request, 'postpage.html', {'post': post})
