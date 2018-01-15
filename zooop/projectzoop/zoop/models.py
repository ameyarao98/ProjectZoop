from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

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


class PostReaction(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    react_type = models.IntegerField(
        validators=[MaxValueValidator(6), MinValueValidator(1)])

    class Meta:
        unique_together = (("post", "user"))

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
