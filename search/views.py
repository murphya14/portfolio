from django.shortcuts import render
from auction.models import hobby_product

# Create your views here.
def do_search(request):
    products = hobby_product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "hobby_product.html", {"products": hobby_product})