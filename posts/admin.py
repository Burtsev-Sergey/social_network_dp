from django.contrib import admin
from posts.models import Post, Comment, Like


# Регистрируем модель Post в административной панели Django
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Определяем поля модели Post, которые:
    # Будут отображаться в списке объектов в админке.
    # Добавляем поиск по полю author.
    list_display = ('author', 'text', 'image', 'created_at')
    search_fields = ('author',)


# Регистрируем модель Comment в административной панели Django
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Определяем поля модели Comment, которые:
    # Будут отображаться в списке объектов в админке.
    # Добавляем поиск по полю author.
    list_display = ('author', 'post', 'text', 'created_at')
    search_fields = ('author',)


# Регистрируем модель Like в административной панели Django
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    # Определяем поля модели Like, которые:
    # Будут отображаться в списке объектов в админке.
    # Добавляем поиск по полю user.
    list_display = ('user', 'post', 'is_active', 'updated_at')
    search_fields = ('user',)
