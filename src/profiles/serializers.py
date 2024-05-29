from rest_framework import serializers 

from django.contrib.auth import get_user_model


class GetUserNetSerializer(serializers.ModelSerializer):
    '''Вывод инфо по user'''

    class Meta:
        model = get_user_model()
        exclude = ('password', 'last_login', 'is_active', 'is_staff', 'is_superuser')