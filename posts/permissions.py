from rest_framework import permissions
from .models import Post

class IsOwnerByHeaderOrJwt(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #if user is authenticated via JWT, match request.user.username
        if request.user and request.user.is_authenticated:
            return getattr(obj, 'username', None) == request.user.username
        username_header = request.headers.get('X-Username')
        return username_header and  username_header == getattr(obj, 'username', None)
    
    