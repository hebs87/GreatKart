from django.shortcuts import render, get_object_or_404

from .models import Product
from categories.models import Category


# Create your views here.
def store(request, category_slug=None):
    """ A view to render the products in the store.html template - allow filtering by category """
    category = None
    products = None

    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
    else:
        products = Product.objects.filter(is_available=True)

    product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }

    return render(request, 'store/store.html', context)


def product_details(request):
    """ A view to render the product-details.html template """

    context = {

    }

    return render(request, 'store/product-details.html', context)
