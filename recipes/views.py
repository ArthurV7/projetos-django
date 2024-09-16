from django.shortcuts import render
from django.http import HttpResponse


def my_viewHome(request):
    return render(request=request, template_name='recipes/index.html')


def my_viewAbout(request):
    return HttpResponse('SOBRE')


def my_viewContact(request):
    return HttpResponse('CONTATO')

