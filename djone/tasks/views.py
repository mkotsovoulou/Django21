from django.http.response import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.urls import reverse
from .models import Task

#global variables
#tasks = ["Cook", "Study", "Clean my Room", "Wash the Car", "Go to the supermarket"]
devname = 'Maira'

# Django can create a Form automatically

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    #priority = forms.IntegerField(label="Prior", min_value=1, max_value=5)


# Create your views here.
def index1(request):
    return render(request, "tasks/index.html", {
        "tasklist" : [],
        "devname" : devname
    })


def index(request):
    if "tasks" not in request.session:  # SESSIONS
        # if the user has not any tasks in the session, create a new one
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        # error no such table: django_session, so we need to
        "tasks": Task.objects.all(),
        #"tasks": request.session["tasks"],
        # create a default table in the database,
        # using the command in the prompt: python manage.py migrate
        "devname": devname
    })


def add1(request):
    return  render(request, "tasks/add.html")

def contactus(request):
    return render(request, "tasks/contactus.html")


def add(request):
    if request.method == "POST":  # submit data
        form = NewTaskForm(request.POST)  # save all data in a variable
        if form.is_valid():  # if form is valid (Server side validation)
            task = form.cleaned_data["task"]  # take all the data from the form
            #request.session["tasks"] += [task]  # append the data into the list
            t = Task(taskname=task)
            t.save()
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form  # pass in the old data
            })
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
