from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.
def list_all_books(request: HttpRequest):
    return HttpResponse("<h1>ALL BOOKS LIST</h1>")


def list_top_books(request: HttpRequest):
    return HttpResponse("<h1>TOP BOOKS LIST</h1>")


def list_free_books(request: HttpRequest):
    return HttpResponse("<h1>FREE BOOKS LIST</h1>")


def list_top_free_books(request: HttpRequest):
    return HttpResponse("<h1>TOP FREE BOOKS LIST</h1>")


def list_classic_books(request: HttpRequest):
    return HttpResponse("<h1>CLASSIC BOOKS LIST</h1>")
