from django.shortcuts import render


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')

def all_products(request):
    """ A view to return the products page """
    return render(request, 'products/products.html', context)