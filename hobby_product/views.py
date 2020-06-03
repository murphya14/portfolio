from django.shortcuts import render

from django.shortcuts import render
from .models import hobby_product

# Create your views here.
def all_hobby_products(request):
    products = hobby_product.objects.all()
    return render(request, "hobby_product.html", {"products": hobby_product})

def home(request):
    """ Return home page """

    return render(request, 'home.html')


def not_found(request):
    """ Return 404 page not found """

    return render(request, '404.html')


def server_error(request):
    """ Return 500 internal server error """

    return render(request, '500.html')