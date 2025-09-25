from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),   # assumes you have views.home
]
