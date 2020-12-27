#!/usr/bin/python
# -*- coding: utf-8 -*-
from hobby_product.models import hobby_product
from datetime import datetime
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def rent(request):
    """ Return rent page """
    return render(request, 'rent.html')

def groups(request):
    """ Return rent page """
    return render(request, 'groups.html')

def private_lessons(request):
    return render(request, 'private_lessons.html')

def summer(request):
    return render(request, 'summer_course.html')

def weekend(request):
    return render(request, 'weekend_course.html')
    
    
def do_search(request):
    """Use keyword to get products"""

    if request.method == 'GET':
        keyword = request.GET.get('q')

        keyword_obj = []

        if keyword is None:
            messages.error(request,
                           'Please enter in a keyword to search')
            return redirect('all_hobby_products')
        elif keyword:
            keyword_lookup = list(hobby_product.objects.filter(Q(name__icontains=keyword) | Q(description__icontains=keyword)))
            
            return render(request, 'hobby_product.html', {'products': keyword_obj})
    else:
        return redirect('all_hobby_products')

def category(request, category):
    """ Show products based on the category selected """
    today = datetime.today()
    product_objects = hobby_product.objects.filter(category=category)

    try:
        product_objects = \
            hobby_product.objects.filter(category=category)
    except:
        messages.info(request,
                      'Sorry there are no products in this category at this time'
                      )
        return redirect('hobby_products')

    paginator = Paginator(product_objects, 6)

    page = request.GET.get('page')
    try:
        product_objects = paginator.page(page)
    except PageNotAnInteger:

        # If the page is not an integer, deliver first page.

        product_objects = paginator.page(1)
    except EmptyPage:

        # If page is not an integer, deliver first page.

        product_objects = paginator.page(paginator.num_pages)

    return render(request, 'category.html',
                  {'products': product_objects, 'category': category})
                  
