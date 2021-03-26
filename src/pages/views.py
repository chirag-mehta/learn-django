from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    print(request.user)
    my_context = {
        'my_message': 'Django is quite awesome! Pleasantly surprised',
        "my_list": [1, 2, 3, 4]
    }
    return render(request, 'home.html', my_context)


def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})
