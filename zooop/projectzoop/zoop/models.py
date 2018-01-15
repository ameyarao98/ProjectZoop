from django.db import models
from django.conf import settings


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET('deleted_user'))
    post_id = models.BigAutoField(primary_key = True)
    content = models.CharField(max_length = 2137)
    timestamp = models.DateTimeField(auto_now_add=True)
    original_poster = models.ForeignKey(settings.AUTH_USER_MODEL,
                                        on_delete=models.SET('deleted_user'),
                                        related_name='author')
    class Meta:
        ordering = ['-timestamp']

class PostReactions(models.Model):
    post  = models.OneToOneField(
        Post,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    react_one = models.IntegerField(default=0)
    react_two = models.IntegerField(default=0)
    react_three = models.IntegerField(default=0)
    react_four = models.IntegerField(default=0)
    react_five = models.IntegerField(default=0)
    react_six = models.IntegerField(default=0)


class UserDetails(models.Model):
    user  = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    description = models.CharField(max_length = 3000)
    avatar = models.ImageField(upload_to = 'avatars/', default = 'default/Think.png')


class Following(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE,
                                    related_name='follows')
    followed_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE,
                                    related_name='followed')

'''
class CustomUser(AbstractBaseUser):
    identifier = models.CharField(max_length=40, unique=True)
    email = models.EmailField()
    USERNAME_FIELD = 'identifier'
'''
