"""
products views.py
"""


from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product
from django.contrib import messages


def all_products(request):
    """ A view to show all products """
    return render(request, 'products/products.html')

    products = Product.objects.all()

    context = {
        'products': products,
    }


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


# end
