from django.shortcuts import render
from django.http import HttpResponse



movies_database = {
    'topgun': 'Top Gun is awesome!',
    'thor': 'Thor is incredible!'
}


def hello(request):
    return HttpResponse('Hello Django!!!')


def movies(request, s):
    client_data = request.GET
    name = client_data.get('name')

    if s in movies_database:
        info = movies_database[s]
        if name is None:
            return HttpResponse(info)
        else:
            return HttpResponse(f'Hello {name}. {info}')
    else:
        return HttpResponse('Movie not found!')
