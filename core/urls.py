from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('settings/', views.settings, name='settings'),
    path('upload/', views.upload, name='upload'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-posts/', views.like_posts, name='like-posts'),
    path('follow/', views.follow, name='follow'),
    path('search/', views.search, name='search'),
]
