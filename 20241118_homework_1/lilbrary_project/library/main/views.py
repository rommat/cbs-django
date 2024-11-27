from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.
def main_page(request: HttpRequest):
    return HttpResponse("<h1>THE MAIN PAGE</h1>")
