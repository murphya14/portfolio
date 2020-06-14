from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from .models import hobby_product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from reviews.models import Review




def all_hobby_products(request):
    try:
        products = hobby_product.objects.all()
    except:
        messages.info(request, 'Sorry there are none in stock at this time')
        return redirect('hobby_product.html')

    paginator = Paginator(products, 6)

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is not an integer, deliver first page.
        products = paginator.page(paginator.num_pages)
    
    return render(request, "hobby_product.html", {"products": products})


def details(request, hobby_product_id):
        """ Return details page """
        product_detail = get_object_or_404(hobby_product, pk=hobby_product_id)

      
        
        return render(request, 'details.html', {'product_detail': product_detail})
