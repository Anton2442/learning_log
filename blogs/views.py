from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


# Create your views here.
def index(request):
    """Домашняя страница"""
    return render(request, 'blogs/index.html')

def posts(request):
    """Список постов"""
    posts = BlogPost.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)

def post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    context = {'post':post}
    return render(request, 'blogs/post.html', context)

@login_required
def new_post(request):
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:posts')
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    if post.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:post', post_id=post_id)
    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
