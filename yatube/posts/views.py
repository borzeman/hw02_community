from django.shortcuts import render, get_object_or_404
from .models import Post, Group

NUM_ART = 10  # Количество выводимых статей


def index(request):
    posts = Post.objects.order_by('-pub_date')[:NUM_ART]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_post(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:NUM_ART]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
