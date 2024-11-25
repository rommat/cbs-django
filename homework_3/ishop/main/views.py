from django.shortcuts import render
from django.http import HttpRequest


# Create your views here.
def main(request: HttpRequest):
    return render(request, 'main/main.html')


def orders_page(request: HttpRequest):
    return render(request, 'main/orders.html')


def contacts_page(request: HttpRequest):
    return render(request, 'main/contacts.html')
 