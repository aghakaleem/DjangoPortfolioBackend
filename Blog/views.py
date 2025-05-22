from django.shortcuts import render
from rest_framework.decorators import api_view
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


    
   