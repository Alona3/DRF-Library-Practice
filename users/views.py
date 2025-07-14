from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from .serializers import UserRegisterSerializer

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.IsAdminUser]
