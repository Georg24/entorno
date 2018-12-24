from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, p):
    primary = p
    posts = Post.objects.filter(pk = primary)
    return render(request, 'blog/post_detail.html', {'posts': posts,'pri':primary})
# Create your views here.
