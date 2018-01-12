from django.urls import path
from django.contrib.auth import views as auth_views

from . import views as core_views

urlpatterns = [
    path('', core_views.index, name='index'),
    path('login', auth_views.login, name='login'),
    path('logout', auth_views.logout, name='logout'),
    path('register', core_views.register, name='register'),
    path('account', core_views.account, name='account'),
    path('add_post', core_views.add_post, name='add_post'),
    path('testing', core_views.testing, name='testing')
]
