import time
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.http import JsonResponse
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from .models import Flight, Passenger


class NewPersonForm(forms.Form):
    lastName = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={'placeholder': 'LastName'}))
    firstName = forms.CharField(label="First Name",  widget=forms.TextInput(attrs={'placeholder': 'FirstName'}))
    avatar = forms.ImageField()
# Create your views here.

# index display a list of all flights
def index(request):
    if not request.user.is_authenticated :
        return HttpResponseRedirect(reverse("login"))

    return render(request, "flights/index.html", {
             "flights" : Flight.objects.all(),
             "passengers" : Passenger.objects.all()

    })

def boot(request):
    return render(request, "flights/boot.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid credentials."
            })
    else:
        return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out."
    })

def newpassenger(request):
    if request.method == "POST":
        form = NewPersonForm(request.POST, request.FILES)
        if form.is_valid():
            ln = form.cleaned_data["lastName"]
            fn = form.cleaned_data["firstName"]
            av = form.cleaned_data["avatar"]
            p = Passenger(first=fn, last = ln, avatar=av)
            p.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "flights/newpassenger.html", {
            "form" : NewPersonForm()
        })


def flight(request, flight_id):
    try:
        flight = Flight.objects.get(id=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight not found.")
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers" : flight.passengers.all(),
        "non_passengers" : Passenger.objects.exclude(flights = flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        try:
            passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
            flight = Flight.objects.get(pk=flight_id)
        except KeyError:
            return HttpResponseBadRequest("Bad Request: no flight chosen")
        except Flight.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: flight does not exist")
        except Passenger.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: passenger does not exist")
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))
    
def posts(request):
    # Get start and end points
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))

    # Generate list of posts
    data = []
    for i in range(start, end + 1):
        data.append(f"Post #{i}")

    # Artificially delay speed of response
    time.sleep(1)

    # Return list of posts
    return JsonResponse({
        "posts": data
    })

def scroll(request):
    return render(request, "flights/scroll.html")

def scroll2(request):
    return render(request, "flights/scroll2.html")
