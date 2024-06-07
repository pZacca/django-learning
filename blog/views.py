from django.shortcuts import render


# Create your views here.


def blog(request):
    print('blog print')
    return render(
        request,
        'blog/blog.html'
    )
