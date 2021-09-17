from django.shortcuts import render


def home(request):
    """ Home view to render index.html template """
    return render(request, 'index.html')
