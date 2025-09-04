from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'username', 'title', 'content', 'created_datetime', 'comments_count','likes_count']
        read_only_fields = ['id', 'created_datetime', 'username','likes_count','comments_count']

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','username', 'title', 'content']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','post','username','content','created_datetime']
        read_only_fields = ['id', 'created_datetime','post']

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','username','content']