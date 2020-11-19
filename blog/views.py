from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Post

def post_list(request):
    posts = Post.objects.order_by('published_date')
    post_links = [(post.title, post.created_date) for post in posts]
    context = {'post_links': post_links}
    return render(request, 'blog/post_list.html', context)
