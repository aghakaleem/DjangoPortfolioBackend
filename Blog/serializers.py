from rest_framework import serializers
from .models import Post, PostSection, Comment, Like
from django.contrib.auth import get_user_model

 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'full_name', 'profile_picture_url']

class PostSectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostSection
        fields = ['id', 'order', 'section_type', 'text', 'image']
        extra_kwargs = {
            'post': {'read_only': True},
            'order': {'required': False},
        }

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'title_image', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at', 'updated_at']
    

class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'user']
        

class PostDetailSerializer(serializers.ModelSerializer):
    sections = PostSectionsSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField() 
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug','title_image', 'created_at', 'updated_at', 'sections', 'comments', 'likes_count', 'comments_count']

    def get_comments_count(self, post):
        return post.comments.count()

    def get_likes_count(self, post):
        return post.likes.count()




