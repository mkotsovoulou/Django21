from django.urls import path
from . import views

urlpatterns = [path("", views.index, name="tasks.index"),
               path("add", views.add, name="tasks.add"),
               path("contactus", views.contactus, name="contactus")
               ]
