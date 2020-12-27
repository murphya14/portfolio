from django.conf.urls import url, include                                                                                                                                                                                                                                                  
from .views import not_found, server_error, home, about

urlpatterns = [
    url('/', home, name='home'),
    url('not_found/', not_found, name='not_found'),
    url('server_error/', server_error, name='server_error'),
    url(r'^about$', about, name='about'),
    
]