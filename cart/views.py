
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from auction.models import Auction, Bid
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def view_cart(request):
    """A View that renders the cart contents page"""
    user = auth.get_user(request)
    auctions = Auction.objects.filter(winner=user).filter(paid=False)
    total = 0 

    for auction in auctions:
        total += auction.winning_bid
    
    context = {
        'auctions': auctions,
        'total': total
    }
    return render(request, "cart.html", context)

@login_required
def add_to_cart(request, auction_id):
    """Add a quantity of the specified product to the cart"""
    auction = get_object_or_404(Auction, pk=auction_id)

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, auction)

    request.session['cart'] = cart
    return redirect(reverse('index'))

@login_required
def adjust_cart(request, auction_id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    auction = get_object_or_404(Auction, pk=auction_id)
    user_default = get_object_or_404(User, pk=1)
    cart = request.session.get('cart', {})

    if auction:
        auction.winner = user_default
        auction.save()
        messages.success(request, 'Product {0} was removed from the cart'.format(auction.hobby_product))
        return redirect('view_cart')
    else:
        messages.error(request, 'Sorry we are unable remove this form your cart')
        return redirect('view_cart')
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

