from django.shortcuts import render
from .models import BlogPost


# Create your views here.
def index(request):
    """Домашняя страница"""
    return render(request, 'blogs/index.html')

def posts(request):
    """Список постов"""
    posts = BlogPost.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)