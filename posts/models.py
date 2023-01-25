from django.db import models

# Create your models here.

class Post(models.Model):
    """post class to manage the post on my app"""
    text  = models.TextField()

    def __str__(self):
        return self.text[:50]
        