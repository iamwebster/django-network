from django.contrib.auth import get_user_model
from .serializers import GetUserNetSerializer, GetUserNetPublicSerializer

from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet


class UserNetPublicView(ModelViewSet):
    '''Вывод публичного профиля пользователя'''
    serializer_class = GetUserNetPublicSerializer
    permission_classes = [permissions.AllowAny]
    queryset = get_user_model().objects.all()


class UserNetView(ModelViewSet):
    '''Вывод профиля пользователя'''
    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return get_user_model().objects.filter(pk=self.request.user.pk)
