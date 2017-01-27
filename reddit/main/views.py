from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html', {'posts': posts})

class Post:
    def __init__(self, date, created_by, name, votes, comments, content):
        self.name = name
        self.date = date
        self.created_by = created_by
        self.votes = votes
        self.comments = comments
        self.content = content

posts = [
        Post(
            datetime.now(),
            "Neil",
            "Post #1",
            0,
            None,
            "Hello world!"),
        Post(
            datetime.now(),
            "Neil",
            "Post #2",
            0,
            None,
            "Hello there!")]
