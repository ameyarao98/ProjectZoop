from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    #user = serializers.PrimaryKeyRelatedField(source='user', read_only=True)
    #original_poster = serializers.PrimaryKeyRelatedField(source='original_poster', read_only=True)

    class Meta:
        model = Post
        fields = ('user' , 'post_id', 'content', 'timestamp', 'original_poster')

class UserDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = 'UserDetails'
        fields = ('user' , 'description')
