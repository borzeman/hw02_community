from django.shortcuts import render, get_object_or_404
from .models import Post, Group, User
import datetime

NUM_ART = 10  # Количество выводимых статей


def index(request):
    author = User.objects.get(username='leo')
    keyword = "утро"
    start_date = datetime.date(1854, 7, 7)
    end_date = datetime.date(1854, 7, 21)
    posts = Post.objects.filter(text__contains=keyword).filter(
      author=author).filter(pub_date__range=(start_date, end_date))

    return render(request, 'posts/index.html', {"posts": posts})


def group_post(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:NUM_ART]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
