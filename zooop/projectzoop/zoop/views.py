from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    current_user = request.user
    print(current_user.username)
    context = {'user': current_user.username}
    return render(request, 'zoop/index.html', context)

def login_view(request):
    return render(request, 'zoop/login_view.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'zoop/signup.html', {'form': form})
