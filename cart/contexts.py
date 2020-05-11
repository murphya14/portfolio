
from django.shortcuts import get_object_or_404
from auction.models import hobby_product, Auction


from django.shortcuts import get_object_or_404
from auction.models import hobby_product


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0

    
    for id in cart.items():
        hobby_product = get_object_or_404(hobby_product, pk=id)
        total = hobby_product.winning_bid
        cart_items.append({'id': id, 'product': hobby_product})
    
    return {'cart_items': cart_items, 'total': total}