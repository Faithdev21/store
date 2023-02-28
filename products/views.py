from django.shortcuts import render


def index(request):
    template = 'products/index.html'
    return render(request, template)


def products(request):
    template = 'products/products.html'
    return render(request, template)
