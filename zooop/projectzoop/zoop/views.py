from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import *
from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request, page_number = 0):

    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit = False)
            new_form.user_id = request.user.id
            new_form.save()
    current_user = request.user
    print(current_user.username)
    posts = Post.objects.all()[10*page_number:10 * (page_number + 1)]
    add_post_form = AddPostForm()
    return render(request, 'zoop/timeline_page.html',
                            {'add_post_form' : add_post_form,
                            'posts' : posts,
                            'visitor' : False})

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

def profile(request, page_number = 0):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit = False)
            new_form.user_id = request.user.id
            new_form.save()
    add_post_form = AddPostForm()
    posts = Post.objects.filter(user_id = request.user.id)[10*page_number:10 * (page_number + 1)]
    return render(request, 'zoop/timeline_page.html',
                            {'add_post_form' : add_post_form,
                            'posts' : posts,
                            'visitor' : False})

def userprofile(request, userid, page_number = 0):
    if request.user.id == userid:
        return profile(request)
    posts = Post.objects.filter(user_id = userid)[10*page_number:10 * (page_number + 1)]
    return render(request, 'zoop/timeline_page.html',
                            {'posts' : posts,
                            'visitor': True})

def testing(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit = False)
            new_form.user_id = request.user.id
            new_form.save()
    add_post_form = AddPostForm()
    posts = Post.objects.filter(user_id = request.user.id)[:10]
    print(posts)
    return render(request, 'zoop/testing.html',
                            {'add_post_form' : add_post_form,
                            'posts' : posts,})
