from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hallo, hier ist der News Index")

def edit(request):
    return HttpResponse("Hier wird ein Artikel bearbeitet")

def detail(request):
    return HttpResponse("Hier wird ein Artikel dargestellt")

# Create your views here.
