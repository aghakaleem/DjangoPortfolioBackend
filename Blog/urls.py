from django.urls import path
from . import views

app_name = 'Blog'

urlpatterns = [
    path('posts', views.PostListView.as_view(), name='post-list'),
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('like_dislike/', views.like_dislike_view, name='like-dislike'),
    path('add_comment/', views.add_comment_view, name='add-comment'),
    path('delete_comment/<int:pk>/', views.delete_comment_view, name='delete-comment'),
    path('update_comment/<int:pk>/', views.update_comment_view, name='update-comment'),
    path('search_posts', views.search_posts_view, name='search-posts'),

]