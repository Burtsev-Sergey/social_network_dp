from django.db import models
from django.contrib.auth import get_user_model


# Создаем модель пользователя.
User = get_user_model()


# Модель для постов. При удалении пользователя — удаляются его посты. 
# Дата и время публикации поста устанавливаются автоматически.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField()
    image = models.ImageField(upload_to='posts/')
    created_at = models.DateTimeField(auto_now_add=True)

    # Метод отображения объекта в админке или в консоли.
    # Показывает автора и первые 20 символов текста.
    def __str__(self):
        return f"{self.author} - {self.text[:20]}"


# Модель для реакций - лайков. user - кто поставил лайк. post - пост, которому поставил лайк.
# is_active - флаг активности лайка - отключаем лайк не удаляя.
# updated_at - время последнего изменения состояния лайка установка/отмена.
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Запрещаем пользователю ставить более одного лайка на один пост.
    class Meta:
        unique_together = ('user', 'post')


# Модель для комментариев к постам. author - автор комментария, post - пост к которому комментарий.
# Дата и время публикации комментария устанавливаются автоматически.
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Метод отображения объекта в админке или в консоли.
    # Показывает автора и первые 20 символов текста.
    def __str__(self):
        return f"{self.author} - {self.text[:20]}"
