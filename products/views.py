from django.shortcuts import render
from .models import Product


def all_products(request):
    """ A view to return the index page """
    return render(request, 'products/products.html', context)

    products = Product.objects.all()

    context = {
        'products': products,
    }