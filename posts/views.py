from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Like
from .serializers import PostSerializer, CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication


# Создание поста. Для доступа требуется токен.
class PostCreateView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Добавление автора/
    # Текущий пользователь автоматически подставляется как создатель поста.
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Получение деталей поста. Для доступа требуется токен.
# Зарегистрированный пользователь получает доступ к деталям каждого поста.
class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Редактирование поста. Для доступа требуется токен.
class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Редактировать пост может только автор поста.
    def get_object(self):
        post = super().get_object()
        if post.author != self.request.user:
            self.permission_denied(
                self.request,
                message="Редактировать может только автор."
                )
        return post


# Создание комментария поста. Для доступа требуется токен.
class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Проверяется наличие указанного поста.
    # Создаются комментарии с автоматическим заполнением полей author и post.
    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)


# Создание/удаление лайка к посту. Для доступа требуется токен.
class LikeCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # При POST-запросе — создать или активировать существующий лайк.
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like, created = Like.objects.get_or_create(
            user=request.user,
            post=post
            )
        like.is_active = True
        like.save()
        return Response({'status': 'liked'}, status=status.HTTP_200_OK)

    # При DELETE-запросе — снять лайк с поста/деактивировать лайк.
    def delete(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like = get_object_or_404(Like, user=request.user, post=post)
        like.is_active = False
        like.save()
        return Response({'status': 'unliked'}, status=status.HTTP_200_OK)
