from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1> Hello World </h1>")

def maira(request) :
    return HttpResponse("<h1> Hello Maira !!!</h1>")
