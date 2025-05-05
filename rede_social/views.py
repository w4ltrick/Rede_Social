from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'pages/index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'pages/post_detail.html', {'post': post})

def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.likes += 1
    post.save()
    return redirect('post_detail', pk=pk)
