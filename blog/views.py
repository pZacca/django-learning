from django.shortcuts import render
from blog.data import posts

# Create your views here.


def blog(request):
    print('blog print')

    context = {
        'text': 'Estamos no Blog',
        'title': 'Blogzao - ',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
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
