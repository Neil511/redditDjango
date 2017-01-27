from __future__ import unicode_literals
from django.db import models

class Post(models.Model):
    name = models.CharField(max_length = 200)
    date = models.DateTimeField(auto_now_add = True)
    created_by = models.CharField(max_length = 100)
    votes = models.IntegerField()
    comments = models.CharField(max_length = 100) #TODO: Update this to take a list of comments
    content = models.TextField()

    def __str__(self):
        return self.name
