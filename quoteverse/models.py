# quoteverse/models.py

from django.contrib.auth.models import User
from django.db import models

class Bookshelf(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Quote(models.Model):
    bookshelf = models.ManyToManyField(Bookshelf)
    text = models.TextField()
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
