from django.conf.urls import url, include                                                                                                                                                                                                                                     
from .views import not_found, server_error, home, about, contact, faq, summer_course

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^about/', about, name='about'),
    url(r'^contact/', contact, name='contact'),
    url(r'^faq/', faq, name='faq'),
    url(r'^summer_course/', summer_course, name='summer_course'),
    url('not_found/', not_found, name='not_found'),
    url('server_error/', server_error, name='server_error'),
    
]