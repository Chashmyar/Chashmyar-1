from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Post


def blog(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)


def blog_single(request, post_title):
    current_post = get_object_or_404(Post, title=post_title)
    context = {
        'post': current_post
    }
    return render(request, 'blog/blog-single.html', context)
