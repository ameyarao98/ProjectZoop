from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Following
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request, page_number = 0):

    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit = False)
            new_form.user_id = request.user.id
            new_form.save()
    current_user = request.user
    posts = Post.objects.filter()[10*page_number:10 * (page_number + 1)]
    #posts_new = Post.objects.filter(following__)
    add_post_form = AddPostForm()
    return render(request, 'zoop/timeline_page.html',
                            {'add_post_form' : add_post_form,
                            'posts' : posts,
                            'visitor' : False,
                            'user_object' : current_user})

def login_view(request):
    return render(request, 'zoop/login_view.html')

def account(request):
    return render(request, 'zoop/account.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'zoop/register.html', {'form': form})


def userprofile(request, userid = -1, page_number = 0):

    if userid == -1:
        userid = request.user.id

    visitor = True
    followed = True
    if request.user.id == userid:
        visitor = False
    else:
        try:
            Following.objects.get(user_id = request.user.id,
                                followed_user_id = userid)
        except ObjectDoesNotExist:
            followed = False



    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit = False)
            new_form.user_id = request.user.id
            new_form.original_poster_id = request.user.id
            new_form.save()
    #print(settings.AUTH_USER_MODEL.models)
    #user = User.objects.get(id = userid)
    user = get_object_or_404(User, id = userid)

    add_post_form = AddPostForm()
    posts = Post.objects.filter(user_id = userid)[10*page_number:10 * (page_number + 1)]
    return render(request, 'zoop/timeline_page.html',
                            {'posts' : posts,
                            'add_post_form' : add_post_form,
                            'visitor': visitor,
                            'followed': followed,
                            'user_object': user})

def testing(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit = False)
            new_form.user_id = request.user.id
            new_form.original_poster_id = request.user.id
            new_form.save()
    add_post_form = AddPostForm()
    posts = Post.objects.filter(user_id = request.user.id)[:10]
    print(posts)
    return render(request, 'zoop/testing.html',
                            {'add_post_form' : add_post_form,
                            'posts' : posts,})

def follow(request, userid):
    Following.objects.get_or_create(user_id = request.user.id,
                            followed_user_id = userid)
    return redirect('/profile/' + str(userid))

def unfollow(request, userid):
    Following.objects.get(user_id = request.user.id,
                            followed_user_id = userid).delete()
    return redirect('/profile/' + str(userid))

def rezoop(request, postid):
    og_post = Post.objects.get(post_id = postid)
    if og_post.user_id != request.user.id:
        Post.objects.get_or_create(user_id = request.user.id,
                            content = og_post.content,
                            original_poster_id = og_post.user_id)
