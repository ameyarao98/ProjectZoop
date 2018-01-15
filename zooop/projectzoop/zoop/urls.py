from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as core_views

from django.conf.urls import url, include
from . import views

from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', core_views.PostViewSet, 'posts')


urlpatterns = [
    path('', core_views.index, name='index'),
    path('login', core_views.login_view, name='login'),
    path('logout', auth_views.logout, name='logout'),
    path('register', core_views.register, name='register'),
    path('account', core_views.account, name='account'),
    path('testing', core_views.testing, name='testing'),
    path('profile', core_views.profile, name='profile'),
    path('profile/<int:userid>/', core_views.userprofile, name='userprofile'),
    path('profile/<int:userid>/<int:page_number>', core_views.userprofile, name='userprofilepage'),
    path('<int:page_number>', core_views.index, name='userprofile'),
    path('rezoop/<int:post_id>/', core_views.rezoop, name='rezoop'),
    path('follow/<int:userid>', core_views.follow, name='follow'),
    path('unfollow/<int:userid>', core_views.unfollow, name='unfollow'),
    path('delete/<int:post_id>', core_views.delete_post, name='delete_post'),
    path('search', core_views.search, name='search'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('upload_avatar', core_views.upload_avatar, name='upload_avatar'),

]
