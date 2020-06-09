from django.shortcuts import render
from hobby_product.models import hobby_product
from datetime import datetime
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages


# Create your views here.
def do_search(request):
    '''Use keyword to get products'''
    products = hobby_product.objects.filter(name__icontains=request.GET['q'])
    
    if request.method == 'GET':
        keyword = request.GET.get('q')

        keyword_obj = []

        if keyword is None or keyword == "":
            messages.error(request, 'Please enter in a keyword to search')
            return redirect('all_lot_items')

        elif keyword:
            keyword_lookup = hobby_product.objects.filter(Q(name__icontains=keyword) | \
                Q(description__icontains=keyword))
            for item in keyword_lookup:
                keyword_obj.append(item)
            


            return render(request, 'hobby_product.html', {"products": hobby_product})
    else:
        return redirect('all_hobby_products')


def category(request, category):
    """ Show products based on the category selected """

    today = datetime.today()
    product_objects = hobby_product.objects.filter(category=category)
    
    try:
        product_objects = hobby_product.objects.filter(category=category)
    except:
        messages.info(request, 'Sorry there are no products in this category at this time')
        return redirect('hobby_products')


    return render(request, 'category.html', {'products': hobby_product, 'category': category})
