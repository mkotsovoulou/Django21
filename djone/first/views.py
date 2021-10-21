from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from models import Flights
def index(request):
    return HttpResponse("<h1> Hello World </h1>")

def maira(request) :
    return HttpResponse("<h1> Hello Maira !!!</h1>")


def flights(request):
    return render(request, "first/flights.html", {
        "flights" : Flights.objects.all()
    })
