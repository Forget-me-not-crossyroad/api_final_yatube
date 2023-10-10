from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Group, Post


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group.
    Поля:
    - id: ID группы (целое число).
    - title: Название группы (строка).
    - slug: Уникальный идентификатор группы (строка).
    - description: Описание группы (строка).
    """
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
