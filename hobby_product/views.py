from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from .models import hobby_product, Review
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from .forms import PostForm


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


def get_reviews(request):
    """
    Create a view that will return a list
    of Posts that were published prior to 'now'
    and render them to the 'posts.html' template
    """
    reviews = Review.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "review.html", {'reviews': reviews})


def review_detail(request, review_id):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    review = get_object_or_404(Review, pk=review_id)
    review.views += 1
    review.save()
    return render(request, "review_detail.html", {'review': review})



def create_or_edit_review(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    review = get_object_or_404(Review, pk=pk) if pk else None
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect(review_detail, review.pk)
    else:
        form = PostForm(instance=review)
    return render(request, 'review_form.html', {'form': form})