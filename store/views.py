from django.shortcuts import render


# Create your views here.
def store(request):
    """ A view to render the products in the store.html template """
    return render(request, 'store/store.html')
