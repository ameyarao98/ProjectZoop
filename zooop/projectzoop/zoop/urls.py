from django.urls import path
from django.contrib.auth import views as auth_views

from . import views as core_views

urlpatterns = [
    path('', core_views.index, name='index'),
    path('login', auth_views.login, name='login'),
    path('logout', auth_views.logout, name='logout'),
    path('register', core_views.register, name='register'),
    path('account', core_views.account, name='account'),
    path('testing', core_views.testing, name='testing'),
    path('profile', core_views.userprofile, name='profile'),
    path('profile/<int:userid>', core_views.userprofile, name='userprofile'),
    path('page/<int:page_number>', core_views.index, name='userprofile'),
    path('rezoop/<int:post_id>', core_views.rezoop, name='rezoop'),
    path('follow/<int:userid>', core_views.follow, name='follow'),
    path('unfollow/<int:userid>', core_views.unfollow, name='unfollow'),
]
