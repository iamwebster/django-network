from rest_framework import serializers 

from django.contrib.auth import get_user_model


class GetUserNetSerializer(serializers.ModelSerializer):
    '''Вывод инфо по user'''

    class Meta:
        model = get_user_model()
        exclude = ('password', 'last_login', 'is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups')


class GetUserNetPublicSerializer(serializers.ModelSerializer):
    '''Вывод публичной инфы по user'''

    class Meta:
        model = get_user_model()
        exclude = (
            'user_permissions', 
            'groups', 
            'email', 
            'password', 
            'last_login', 
            'is_active', 
            'is_staff', 
            'is_superuser',
            'phone',
        )