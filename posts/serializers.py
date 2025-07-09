from rest_framework import serializers
from .models import Post, Comment, Like


# Сериализатор для Comment. В API выводит поля: `author`, `text`, `created_at`.
# Поля author' и 'created_at сериализатор не меняет - определяются автоматически.
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'text', 'created_at']
        read_only_fields = ['author', 'created_at']


# Сериализатор для Post. В API выводит поля id, text, image, created_at и добавляет поля:
#  comments — список сериализованных комментариев к посту.
#  likes_count — количество лайков поста.
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'text', 'image', 'created_at', 'comments', 'likes_count']

    # Метод сериализатора. Возвращает количество активных лайков для текущего поста.
    def get_likes_count(self, obj):
        return obj.likes.filter(is_active=True).count()
