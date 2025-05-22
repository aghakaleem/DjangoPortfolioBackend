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
@permission_classes([IsAuthenticated])
def create_comment_view(request):
    user = get_user_model().objects.get(email=request.email)
    post = Post.objects.get(slug=request.slug)

    content = request.data.get('content')
    if not content:
        return Response({"error": "Content is required."}, status=status.HTTP_400_BAD_REQUEST)
    
    comment = Comment.objects.create(user=user, post=post, content=content)
    serializer = CommentSerializer(comment)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def like_dislike_view(request):
    user = get_user_model().objects.get(email=request.email)
    post = Post.objects.get(slug=request.slug)

    if request.method == 'DELETE':
        if Like.objects.filter(user=user, post=post).exists():
            # If the like exists, delete it (dislike)
            like = Like.objects.get(user=user, post=post)
            like.delete()
            return Response({"message": "Like removed."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return
    else: 
        # If the like does not exist, create it (like)
        if not Like.objects.filter(user=user, post=post).exists():
            like = Like.objects.create(user=user, post=post)
            serializer = LikeSerializer(like)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
    
    






    
   