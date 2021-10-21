from django.urls import path
from . import views

urlpatterns = [path("", views.flights, name="flights"),
               path ('maira', views.maira, name="maira"),
               ]
