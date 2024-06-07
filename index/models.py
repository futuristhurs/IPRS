from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class User(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
  profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=50)
  username = models.CharField(max_length=50, unique=True)
  
  def __str__(self):
    return f'{self.user.username} Profile'
  
