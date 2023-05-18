from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def produto_lista(request):
    return render(request, 'produtos.html')

def produto_detalhe(request):
    return render(request, 'produto_detalhes.html')