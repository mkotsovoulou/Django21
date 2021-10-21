from django.urls import path
from . import views

urlpatterns = [path ("", views.index, name="index"),
               path ('maira', views.maira, name="maira"),
               path('flights', views.flights, name="flights")
               ]
