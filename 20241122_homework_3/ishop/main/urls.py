from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='homepage'),
    path('orders/', orders_page, name='orders_page'),
    path('contacts/', contacts_page, name='contacts_page'),
    path('categories/<int:category_id>/', category_page, name='category_page'),
    path('categories/<int:category_id>/product/<int:product_id>', product_page, name='product_page'),
]
