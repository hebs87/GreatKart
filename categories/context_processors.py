from .models import Category


def menu_links(request):
    """ Returns the Categories to the any template that calls it """
    categories = Category.objects.all()
    return dict(categories=categories)
