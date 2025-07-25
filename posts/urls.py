from django.urls import path
from .views import (
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    CommentCreateView,
    LikeCreateView,
    )


# Список маршрутов:
# post-create создание поста, post-detail получение деталей поста.
# post-edit редактирование поста. comment-create создание комментария к посту.
# like-create создание/отмена лайка к посту.
urlpatterns = [
    path(
        'posts/',
        PostCreateView.as_view(),
        name='post-create',
        ),
    path(
        'posts/<int:pk>/',
        PostDetailView.as_view(),
        name='post-detail',
        ),
    path(
        'posts/<int:pk>/edit/',
        PostUpdateView.as_view(),
        name='post-edit',
        ),
    path(
        'posts/<int:post_id>/comments/',
        CommentCreateView.as_view(),
        name='comment-create',
        ),
    path(
        'posts/<int:post_id>/like/',
        LikeCreateView.as_view(),
        name='like-create',
        ),
]
