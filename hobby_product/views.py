from django.shortcuts import render
from .models import hobby_product

# Create your views here.
def all_hobby_products(request):
    hobby_products = hobby_product.objects.all()
    return render(request, "hobby_product.html", {"products": hobby_products})