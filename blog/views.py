from django.shortcuts import render
from blog.data import posts
from typing import Any
from django.http import HttpRequest, Http404
# Create your views here.


def blog(request):
    print('blog print')

    context = {
        'text': 'Estamos no Blog',
        'title': 'Blogzao - ',
        'posts': posts,
    }

    return render(
        request,
        'blog/index.html',
        context
    )


def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = next(
        (post for post in posts if post['id'] == post_id), None)

    if found_post is None:
        raise Http404('Post não existe.')

    context = {
        'text': ' ',
        'title': found_post['title'] + ' - ',
        'post': found_post,
    }

    return render(
        request,
        'blog/post.html',
        context
    )


def zacca(request):
    print('zacca print')

    context = {
        'text': 'Estamos no Zacca',
        'title': 'Zaccao - '
    }

    return render(
        request,
        'blog/zacca.html',
        context
    )
