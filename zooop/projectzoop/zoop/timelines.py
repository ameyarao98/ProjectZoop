from .models import Post
from django.contrib.auth.models import User

def get_user_timeline(user_id, start_index):
    user = get_object_or_404(User, pk=user_id)
    posts = Post.objects.filter(user = user)

def add_post(request):
    user = get_object_or_404(User, pk=user_id)
    new_post = Post(user = user, content = content)
