from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='homepage'),
    path('orders/', orders_page, name='orders_page'),
    path('contacts/', contacts_page, name='contacts_page'),
]
