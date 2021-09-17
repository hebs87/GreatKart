from django.shortcuts import render
from store.models import Product


def home(request):
    """ Home view to render index.html template and return all active products """
    products = Product.objects.filter(is_available=True)

    context = {
        'products': products,
    }

    return render(request, 'index.html', context)
