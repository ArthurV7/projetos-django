from django.shortcuts import render
from django.http import HttpResponse


def my_viewHome(request):
    return HttpResponse('HOME')


def my_viewAbout(request):
    return HttpResponse('SOBRE')


def my_viewContact(request):
    return HttpResponse('CONTATO')

