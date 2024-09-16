from django.shortcuts import render


def my_viewHome(request):
    # recebe as informações da requisição HTTP feita pelo cliente, processa essas informações, renderiza uma página HTML, e entrega como uma resposta HTTP.
    return render(request=request, template_name='recipes/index.html')


def my_viewAbout(request):
    return render(request=request, template_name='recipes/about.html')


def my_viewContact(request):
    data = {
        'name': 'Arthur',
        'age': 18,
        'birth_date': '07/04/2006'
    }
    return render(request=request, template_name='recipes/contact.html', context=data)

