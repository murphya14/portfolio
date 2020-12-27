from django.shortcuts import render, redirect, reverse
from hobby_product.models import hobby_product



def home(request):
    """ Return home page """
    #return redirect(reverse('home'))
    return render(request, 'home.html')


def not_found(request):
    """ Return 404 page not found """

    return render(request, '404.html')


def server_error(request):
    """ Return 500 internal server error """

    return render(request, '500.html')

def about(request):
    return render(
        request, "about.html"
    )
