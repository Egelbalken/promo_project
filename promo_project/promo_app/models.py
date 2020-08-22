from django.db import models

# Create your models here.
class User(models.Model):
    """docstring for models."""
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.EmailField(max_length=264,unique=True)
