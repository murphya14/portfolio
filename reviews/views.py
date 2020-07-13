from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReviewForm
from .models import Review
import datetime
from django.conf import settings
from hobby_product.models import hobby_product
from django.contrib.auth.models import User

def product_review(request, id):
    product = get_object_or_404(hobby_product, pk=id)
    reviews = Review.objects.filter(product = id).order_by('-published_date')[:5]
    return render(request, "review.html", {"reviews":reviews, "product":product})


@login_required
def add_review(request, id):
    product = get_object_or_404(hobby_product, pk=id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.author = request.user
            form.save()
            products = hobby_product.objects.all()
        return redirect('all_hobby_products')
    else:
        form=ReviewForm()
        return render(request, "create_review.html", {'product': product, 'form': form}) 