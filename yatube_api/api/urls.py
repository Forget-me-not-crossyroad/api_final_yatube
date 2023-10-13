from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'

# Регистрация Viewsets и эндпоинтов
v1_router = DefaultRouter()
v1_router.register('follow', FollowViewSet, basename='followings')
v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register('groups', GroupViewSet)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)

urlpatterns = [
    path(
        'v1/', include(v1_router.urls)
    ),  # Вторая часть префикса для всех эндпоинтов
    path(
        'admin/', admin.site.urls
    ),  # Эндпоинт для админки (для создания Groups)
    path(
        'v1/', include('djoser.urls.jwt'),
    ),  # Эндпоинт для получения Token
]
