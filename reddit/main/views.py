from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def data(request):
    posts = Post.objects.all()
    form = PostForm()
    return render(request, 'data.html', {'posts': posts, 'form': form})

def posts(request, post_id):
    post = Post.objects.get(id = post_id)
    return render(request, 'postpage.html', {'post': post})

def user(request, username):
    name = username
    return render(request, 'user.html', {'name': name})

def new_post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = Post(name = form.cleaned_data['name'],
                    created_by = form.cleaned_data['created_by'],
                    votes = 0,
                    comments = [],
                    content = form.cleaned_data['content'])
        post.save()
        return HttpResponseRedirect('/data')
