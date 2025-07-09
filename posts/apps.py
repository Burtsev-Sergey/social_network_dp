from django.apps import AppConfig


# Создаем класс конфигурации для приложения posts, который наследуется от AppConfig
class PostsConfig(AppConfig):
    # Указываем тип поля для автоматического увеличения идентификаторов моделей. Задаем имя приложения
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
