from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from django.urls import reverse
# Create your models here.

class Contact(models.Model):
    Name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.TextField(null=True, blank=True)
    message = models.TextField()

class Post(models.Model):
    """
    docstring
    """
    postid = models.AutoField(primary_key=True)
    thumbnail = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=105)
    pub_date = models.DateField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    def __str__(self):
        return self.title