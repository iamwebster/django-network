from django.contrib import admin
from .models import Comment, Post
from mptt.admin import MPTTModelAdmin


@admin.register(Post)
class CommentAdmin(admin.ModelAdmin):
    '''Посты'''
    list_display = ('user', 'published', 'create_date', 'moderation', 'view_count', 'id')

@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    '''Комментарии к постам'''
    list_display = ('user', 'post', 'created_date', 'updated_date', 'published', 'id')
    mptt_level_indent = 15