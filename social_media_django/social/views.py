from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Post, Comment, Like, Follow

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'social/index.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'social/post_detail.html', {'post': post, 'comments': comments})
