from django.conf.urls import url, include                                                                                                                                                                                                                                                  
from .views import home, not_found, server_error

urlpatterns = [
    url('', home, name='home'),
    url('not_found/', not_found, name='not_found'),
    url('server_error/', server_error, name='server_error')
]