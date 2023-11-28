from django.contrib import admin
from django.urls import path
from . import views


app_name = 'blogs'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница со списком всех записей.
    path('posts/', views.posts, name='posts'),
]
