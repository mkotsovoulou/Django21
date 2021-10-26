from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

#global variables
tasks = ["Cook", "Study", "Clean my Room", "Wash the Car", "Go to the supermarket"]

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasklist" : tasks
    })
