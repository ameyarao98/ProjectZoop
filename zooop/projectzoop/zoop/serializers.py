from django.contrib.auth.models import User, Group
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = 'Post',
        fields = ('user' , 'post_id', 'content', 'timestamp', 'original_poster')

class UserDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = 'UserDetails',
        fields = ('user' , 'description')
