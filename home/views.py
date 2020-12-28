from django.shortcuts import render, redirect, reverse
from hobby_product.models import hobby_product



def home(request):
    """ Return home page """
    #return redirect(reverse('home'))
    return render(request, 'home.html')


def groups(request):
    """ Return home page """
    #return redirect(reverse('home'))
    return render(request, 'groups.html')

def private_lessons(request):
    """ Return home page """
    #return redirect(reverse('home'))
    return render(request, 'private_lessons.html')

def weekend_course(request):
    """ Return home page """
    #return redirect(reverse('home'))
    return render(request, 'weekend_course.html')

def contact(request):
    """ Return home page """
    #return redirect(reverse('home'))
    return render(request, 'contact.html')

def summer_course(request):
    """ Return home page """
    #return redirect(reverse('home'))
    return render(request, 'summer_course.html')

def faq(request):
    """ Return home page """
    #return redirect(reverse('home'))
    return render(request, 'faq.html')


def not_found(request):
    """ Return 404 page not found """

    return render(request, '404.html')


def server_error(request):
    """ Return 500 internal server error """

    return render(request, '500.html')

def about(request):
    """ Return about.html """

    return render(request, 'about.html')


