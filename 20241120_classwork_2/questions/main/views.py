from django.shortcuts import render
from django.http import HttpRequest


# Create your views here.
def main(request: HttpRequest):
    return render(request, "main/index.html")
