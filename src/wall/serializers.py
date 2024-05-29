from rest_framework import serializers

from ..base.serializers import RecursiveSerializer, FilterCommentListSerializer
from .models import Post, Comment


class CreateCommentSerializer(serializers.ModelSerializer):
    """ Добавление комментариев к посту
    """
    class Meta:
        model = Comment
        fields = ("post", "text", "parent")


class ListCommentSerializer(serializers.ModelSerializer):
    """ Список комментариев
    """
    text = serializers.SerializerMethodField()
    children = RecursiveSerializer(many=True)
    user = serializers.ReadOnlyField(source='user.username')
    post = serializers.IntegerField(write_only=True)

    def get_text(self, obj):
        if obj.deleted:
            return None
        return obj.text

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ("id", "post", "user", "text", "created_date", "updated_date", "deleted", "children")


class PostSerializer(serializers.ModelSerializer):
    """ Вывод и редактирование поста
    """
    user = serializers.ReadOnlyField(source='user.username')
    comments = ListCommentSerializer(many=True, read_only=True)
    view_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ("id", "create_date", "user", "text", "comments", "view_count")


class ListPostSerializer(serializers.ModelSerializer):
    """ Список постов
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = ("id", "create_date", "user", "text", "comments_count")