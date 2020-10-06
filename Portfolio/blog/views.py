from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')  # it grabs all database objects and turns them into python obj
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)  # pk - PRIMARY KEY
    return render(request, 'blog/detail.html', {'blog': blog})
