<<<<<<< HEAD
from rest_framework import viewsets, permissions
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAdminOrReadOnly


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 9584a163bf5bf3143aa5843d8161258c3f89a918
