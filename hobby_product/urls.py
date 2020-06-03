from django.conf.urls import url, include
from .views import all_hobby_products, home, not_found, server_error

urlpatterns = [
    url(r'^$', all_hobby_products, name='all_hobby_products'),
    url(r'^home/$', home, name='home'),
    url('not_found/', not_found, name='not_found'),
    url('server_error/', server_error, name='server_error')
]