from django.contrib import admin
from django.urls import path
from . import views


app_name = 'blogs'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница со списком всех записей.
    path('posts/', views.posts, name='posts'),
    # Страница с конкретной записью
    path('posts/<int:post_id>', views.post, name='post'),
    # Страница для создания поста
    path('new_post', views.new_post, name='new_post'),
    # Страница для редактирования поста
    path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),
]
