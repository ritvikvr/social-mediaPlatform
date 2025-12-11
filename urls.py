
from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('feed/', views.feed, name='feed'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:pk>/comment/', views.comment_create, name='comment_create'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('search/', views.search_users, name='search_users'),
]
