from rest_framework import serializers
from .models import Post, Comment, Like



# Сериализатор для валидации картинок. 
# Проверяет: формат картинки; в файле есть картинка; файл с картинкой пустой; 
# поле картинки отсутствует в запросе.
class CustomImageField(serializers.ImageField):
    default_error_messages = {
        'invalid_image': 'Допустимы только картинки jpg, png, gif.',
        'invalid': 'Загружен некорректный файл. Допустимы только изображения.',
        'empty': 'Файл изображения не может быть пустым.',
        'required': 'Изображение обязательно для загрузки.' 
    }


# Сериализатор для Comment. В API выводит поля: `author`, `text`, `created_at`.
# Поля author' и 'created_at сериализатор не меняет - определяются автоматически.
# Валидация отсутствия поля комментария в запросе или пустой строки комментария.
# Валидация длины комментария - не больше 300 символов. 
class CommentSerializer(serializers.ModelSerializer):
    text = serializers.CharField(
        required=True,
        error_messages={
            'required': 'Комментарий не может быть пустым.',
            'blank': 'Комментарий не может быть пустым.'
        }
    ) 


    class Meta:
        model = Comment
        fields = ['author', 'text', 'created_at']
        read_only_fields = ['author', 'created_at']


    # Метод сериализатора. Валидация длины текста комментария - не больше 300 символов. 
    def validate_text(self, value):
        if len(value) > 300:
            raise serializers.ValidationError('Комментарий должен быть меньше 300 символов.')
        return value    


# Сериализатор для Post. В API выводит поля id, text, image, created_at и добавляет поля:
#  comments — список сериализованных комментариев к посту.
#  likes_count — количество лайков поста.
# Валидация отсутствия поля поста в запросе или пустой строки поста.
# Валидация длины текста поста - не больше 3000 символов.
# Валидация картинки: формат файла; наличие файла; размер файла.    
class PostSerializer(serializers.ModelSerializer):
    image = CustomImageField()
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    text = serializers.CharField(
        required=True,
        error_messages={
            'required': 'Текст поста не может быть пустым.',
            'blank': 'Текст поста не может быть пустым.'
        }
    )    


    class Meta:
        model = Post
        fields = ['id', 'text', 'image', 'created_at', 'comments', 'likes_count']


    # Метод сериализатора. Валидация длины текста поста - не больше 3000 символов. 
    def validate_text(self, value):
        if len(value) > 3000:
            raise serializers.ValidationError('Длина поста не должна превышать 3000 символов.')
        return value


    # Метод сериализатора. Валидация размера картинки - не больше 2 Мб
    def validate_image(self, value):
        if value.size > 2*1024*1024:
            raise serializers.ValidationError('Размер картинки не должен превышать 2 Мб.')
        return value


    # Метод сериализатора. Возвращает количество активных лайков для текущего поста.
    def get_likes_count(self, obj):
        return obj.likes.filter(is_active=True).count()
