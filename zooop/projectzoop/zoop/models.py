from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET('deleted_user'))
    post_id = models.BigAutoField(primary_key = True)
    content = models.CharField(max_length = 2137)
    timestamp = models.DateTimeField(auto_now_add=True)

class UserDetails(models.Model):
    #avatar =
    #description =
    pass

class Following(models.Model):
    #current_user =
    pass

'''
class CustomUser(AbstractBaseUser):
    identifier = models.CharField(max_length=40, unique=True)
    email = models.EmailField()
    USERNAME_FIELD = 'identifier'
'''
