from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

PRE_TEXT_LEN: int = 15  # Длина текста превью


class Group(models.Model):
    """Модель группы (сообщество)."""

    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок',
        help_text='Название категории, не более 200 символов',
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text=(
            'Идентификатор страницы для URL; разрешены символы'
            ' латиницы, цифры, дефис и подчёркивание.'
        ),
    )
    description = models.TextField(
        verbose_name='Описание', help_text='Описание категории, текстовое поле'
    )

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'Группы'
        ordering = ('title',)

    def __str__(self):
        return self.title[:PRE_TEXT_LEN]


class Post(models.Model):
    """Модель поста."""

    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name='Группа постов',
        help_text='Группа поста',
    )

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.text[:PRE_TEXT_LEN]


class Comment(models.Model):
    """Модель комментария."""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )


class Follow(models.Model):
    """Модель подписки."""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follows'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='following',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_user_following',
            )
        ]
