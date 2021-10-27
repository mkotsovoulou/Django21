from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

#global variables
tasks = ["Cook", "Study", "Clean my Room", "Wash the Car", "Go to the supermarket"]
devname = 'Maira';
# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasklist" : tasks,
        "devname" : devname
    })

def add(request):
    return  render(request, "tasks/add.html")

def contactus(request):
    return render(request, "tasks/contactus.html")
