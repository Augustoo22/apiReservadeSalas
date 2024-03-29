from django.shortcuts import render

def minha_view(request):
    context = {'chave': 'valor'}  # Contexto opcional para passar dados para o template
    return render(request, 'meuapp/template.html', context)
