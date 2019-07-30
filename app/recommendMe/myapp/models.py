from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    following = models.CharField(max_length=10000)
    postsCaption = models.CharField(max_length=10000)
    categorie = models.CharField(max_length=100)