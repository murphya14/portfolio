
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from hobby_product.models import hobby_product
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


@login_required
def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    hobby_products = hobby_product.objects.all()
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('home'))


@login_required
def remove_cart_item(request, product_id):
    """ Remove single product item """
    cart = request.session.get('cart', {})

    if product_id in cart:
        cart.pop(product_id)
        messages.success(request, 'Successfully removed item')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))