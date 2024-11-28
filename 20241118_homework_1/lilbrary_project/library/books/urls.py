from django.urls import path
from .views import *

urlpatterns = [
    path('', list_all_books),
    path('top/', list_top_books),
    path('free/', list_free_books),
    path('top/free/', list_top_free_books),
    path('oldschool/', list_classic_books),
]
