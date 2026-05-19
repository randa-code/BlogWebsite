from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post, Comment, Category

def main_view(request):
    return render(request, 'blog/main.html')

def users_view(request):
    users = User.objects.all()
    return render(request, 'blog/users.html', {'users': users})

def blogs_view(request):
    posts = Post.objects.all()
    return render(request, 'blog/blogs.html', {'posts': posts})

def comments_view(request):
    comments = Comment.objects.all()
    return render(request, 'blog/comments.html', {'comments': comments})

def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'blog/categories.html', {'categories': categories})

def blog_details_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/blogdetails.html', {'post': post})