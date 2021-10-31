from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
  path ("", views.index, name="index"),
  path("<int:flight_id>", views.flight, name="flight"),
  path("<int:flight_id>/book", views.book, name="book"),
  path("posts", views.posts, name="posts"),
  path("scroll", views.scroll, name="scroll"),
  path("scroll2", views.scroll2, name="scroll2"),
  path("login", views.login_view, name="login"),
  path("logout", views.logout_view, name="logout"),
  path("add", views.newpassenger, name="add"),
  path("boot", views.boot, name="boot")
] 
