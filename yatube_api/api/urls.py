from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet

app_name = 'api'

# Регистрация Viewsets и эндпоинтов
v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet)
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
        'v1/api-token-auth/', views.obtain_auth_token
    ),  # Эндпоинт для получения Token
]