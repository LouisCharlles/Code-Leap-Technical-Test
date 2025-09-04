from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Post, Comment
from rest_framework.decorators import action
from .serializers import (
    PostSerializer,
    PostCreateSerializer,
    CommentSerializer,
    CommentCreateSerializer,
)
from .permissions import IsOwnerByHeaderOrJwt


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_datetime')
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['created_datetime']
    filterset_fields = ['username']


    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsOwnerByHeaderOrJwt()]
        return []


    def get_serializer_class(self):
        if self.action == 'create':
            return PostCreateSerializer
        return PostSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save()
        out_serializer = PostSerializer(post)
        return Response(out_serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=True,methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        post.likes_count+=1
        post.save()
        return Response({'status':'liked','likes_count':post.likes_count})
    
    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        post = self.get_object()
        if post.likes_count > 0:
            post.likes_count -= 1
            post.save()
        return Response({'status': 'unliked', 'likes_count': post.likes_count})

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_datetime')


    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsOwnerByHeaderOrJwt()]
        return []


    def get_serializer_class(self):
        if self.action == 'create':
            return CommentCreateSerializer
        return CommentSerializer


    def create(self, request, *args, **kwargs):
        post_id = self.kwargs.get('post_pk')
        post = Post.objects.get(pk=post_id)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save(post=post)  # passa a instância do post
        out_serializer = CommentSerializer(comment)
        return Response(out_serializer.data, status=status.HTTP_201_CREATED)

