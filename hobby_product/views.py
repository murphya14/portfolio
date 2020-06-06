from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from .models import hobby_product

# Create your views here.
def all_hobby_products(request):
    try:
        products = hobby_product.objects.all()
    except:
        messages.info(request, 'Sorry there are none in stock at this time')
        return redirect('hobby_product')

    
    return render(request, "hobby_product.html", {"products": hobby_product})


def details(request, hobby_product_id):
        """ Return details page """
        hobby_product = get_object_or_404(hobby_product, pk=hobby_product_id)
        return render(request, 'details.html', {'hobby_product': hobby_product})




    
    