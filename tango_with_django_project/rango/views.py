
from django.shortcuts import render

from django.http import HttpResponse
def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)


def About(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return HttpResponse(request,'rango/about.html', context=context_dict)
