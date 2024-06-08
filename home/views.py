from django.shortcuts import render


# Create your views here.


def home(request):
    print('home print')

    context = {
        'text': 'Estamos na Home'
    }

    return render(
        request,
        'home/index.html',
        context
    )
