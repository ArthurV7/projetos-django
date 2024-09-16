from django.shortcuts import render


def my_viewHome(request):
    return render(request=request, template_name='recipes/index.html')


def my_viewAbout(request):
    return render(request=request, template_name='recipes/about.html')


def my_viewContact(request):
    return render(request=request, template_name='recipes/contact.html')

