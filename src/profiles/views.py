from django.contrib.auth import get_user_model 
from .serializers import GetUserNetSerializer

from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework import permissions


class GetUserNetView(RetrieveAPIView):
    '''Вывод профиля пользователя'''
    queryset = get_user_model().objects.all()
    serializer_class = GetUserNetSerializer


class UpdateUserNetView(UpdateAPIView):
    '''Редактирование пользователя'''
    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return get_user_model().objects.filter(id=self.request.user.id)