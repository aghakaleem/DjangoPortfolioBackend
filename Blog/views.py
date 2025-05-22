from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q
from .models import Post, PostSection, Comment, Like
from rest_framework.response import Response
from rest_framework import generics
from .serializers import PostListSerializer, PostDetailSerializer, CommentSerializer, LikeSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostDetailView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def add_comment_view(request):
    email = request.data.get('email')
    slug = request.data.get('slug')
    if not email or not slug:
        return Response({"error": "Email and slug are required."}, status=status.HTTP_400_BAD_REQUEST)
    
    user = get_user_model().objects.get(email=email)
    post = Post.objects.get(slug=slug)

    content = request.data.get('content')
    if not content:
        return Response({"error": "Content is required."}, status=status.HTTP_400_BAD_REQUEST)
    
    comment = Comment.objects.create(user=user, post=post, content=content)
    serializer = CommentSerializer(comment)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def delete_comment_view(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    
        if comment:
            comment.delete()
            return Response({"message": "Comment deleted."}, status=status.HTTP_204_NO_CONTENT)
    except Comment.DoesNotExist:
        return Response({"error": "Comment not found."}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def update_comment_view(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response({"error": "Comment not found."}, status=status.HTTP_404_NOT_FOUND)
    
    content_text = request.data.get('content')
    if not content_text:
        return Response({"error": "Content is required."}, status=status.HTTP_400_BAD_REQUEST)
    
    comment.content = content_text
    comment.save()
    serializer = CommentSerializer(comment)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def like_dislike_view(request):
    email = request.data.get('email')
    slug = request.data.get('slug')
    if not email or not slug:
        return Response({"error": "Email and slug are required."}, status=status.HTTP_400_BAD_REQUEST)
    
    user = get_user_model().objects.get(email=email)
    post = Post.objects.get(slug=slug)

    if Like.objects.filter(user=user, post=post).exists():
        # If the like exists, delete it (dislike)
        like = Like.objects.get(user=user, post=post)
        like.delete()
        return Response({"message": "Like removed."}, status=status.HTTP_204_NO_CONTENT)
    else: 
        # If the like does not exist, create it (like)
        like = Like.objects.create(user=user, post=post)
        serializer = LikeSerializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    
@api_view(['GET'])
def search_posts_view(request):
    query = request.query_params.get("query")
    if not query:
        return Response({"error": "Query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    posts = Post.objects.filter(Q(title__icontains=query) | Q(sections__text__icontains=query)).distinct()
    serializer = PostListSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)





    
   