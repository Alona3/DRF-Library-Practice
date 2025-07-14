from rest_framework import viewsets, permissions
<<<<<<< HEAD
from rest_framework_simplejwt.authentication import JWTAuthentication
=======
>>>>>>> 9584a163bf5bf3143aa5843d8161258c3f89a918
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class BookViewSet(viewsets.ModelViewSet):
<<<<<<< HEAD
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
=======
>>>>>>> 9584a163bf5bf3143aa5843d8161258c3f89a918
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]
