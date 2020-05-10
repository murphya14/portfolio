
from django.shortcuts import get_object_or_404
from auction.models import hobby_product, Auction


def cart_contents(request, auction):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    hobby_product_count = 0
    
    for auction_id in cart.items(auction_id):
        hobby_product = get_object_or_404(hobby_product, pk=auction_id)
        total = auction.winning_bid
      
        cart_items.append({'id': auction_id, 'product': hobby_product})
    
    return {'cart_items': cart_items, 'total': total, 'product_count': hobby_product_count}


