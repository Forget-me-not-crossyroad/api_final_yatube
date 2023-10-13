from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post.

    Поля:
    - id: ID поста (целое число).
    - text: Текст поста (строка).
    - author: Автор поста (только для чтения, строка - имя пользователя).
    - image: Изображение поста (строка - URL изображения).
    - group: Группа, к которой относится пост (целое число - ID группы).
    - pub_date: Дата публикации поста (дата и время).
    """

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
    """Сериализатор для модели Comment.

    Поля:
    - id: ID комментария (целое число).
    - author: Автор комментария (только для чтения, строка - имя пользователя).
    - post: Пост, к которому относится комментарий (целое число - ID поста).
    - text: Текст комментария (строка).
    - created: Дата создания комментария (дата и время).
    """

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Follow.

    Поля:
    - user: пользователь, на которого выполняется подписка.
    - following: подписки пользователя.
    """

    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault(),
    )
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('following', 'user'),
                message='Вы уже подписаны на этого пользователя.',
            )
        ]

    def validate(self, attrs):
        if self.context['request'].user == attrs['following']:
            raise serializers.ValidationError(
                'Вы не можете подписаться на себя.'
            )
        return attrs
