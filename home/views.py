from django.shortcuts import render, redirect, reverse
from hobby_product.models import hobby_product
from django.core.mail import send_mail
from django.http import HttpResponse 
from home.forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage




# add to your views
def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['celticsurfschool@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })

def home(request):
    """ Return home page """
    #return redirect(reverse('home'))
    return render(request, 'home.html')

# Create your views here.
def rent(request):
    """ Return rent page """
    return render(request, 'rent.html')

# Create your views here.
def gallery(request):
    """ Return rent page """
    return render(request, 'gallery.html')


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


