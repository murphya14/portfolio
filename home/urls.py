from django.conf.urls import url, include                                                                                                                                                                                                                                     
from .views import not_found, server_error, home, about, contact, faq, project_four, project_five, project_one, project_two, project_three, project_six, portfolio

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^about/', about, name='about'),
    url(r'^contact/', contact, name='contact'),
    url(r'^faq/', faq, name='faq'),
    url(r'^project_four/', project_four, name='project_four'),
    url(r'^project_five/', project_five, name='project_five'),
    url(r'^project_one/', project_one, name='project_one'),
    url(r'^project_two/', project_two, name='project_two'),
    url(r'^project_three/', project_three, name='project_three'),
    url(r'^project_six/', project_six, name='project_six'),
    url(r'^portfolio/', portfolio, name='portfolio'),
    url('not_found/', not_found, name='not_found'),
    url('server_error/', server_error, name='server_error'),
    
]