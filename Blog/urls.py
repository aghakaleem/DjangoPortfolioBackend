from django.urls import path
from . import views

app_name = 'Blog'

urlpatterns = [
    path('posts', views.PostListView.as_view(), name='post-list'),
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('create_comment/', views.create_comment_view, name='create-comment'),
    path('like_dislike/', views.like_dislike_view, name='like-dislike'),


]