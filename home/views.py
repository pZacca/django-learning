from django.shortcuts import render


# Create your views here.


def home(request):
    print('home print')
    return render(
        request,
        'home/index.html'
    )
