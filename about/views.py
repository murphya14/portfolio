from django.shortcuts import render
from django.shortcuts import render, redirect, reverse
from hobby_product.models import hobby_product

def home(request):
    """ Return home page """
    #return redirect(reverse('home'))
    return render(request, 'home.html')

def about(request):
    """ Return about page """
    #return redirect(reverse('home'))
    return render(request, 'about.html')

