from django.shortcuts import render


def my_viewHome(request):
    # recebe as informações da requisição HTTP feita pelo cliente, processa essas informações, renderiza uma página HTML, e entrega como uma resposta HTTP.
    return render(request=request, template_name='recipes/index.html')

