from django.urls import path
from . import views

urlpatterns = [

    path("", views.index, name="index"),
    path("index", views.index),
    path("tumu", views.index),
    path("<slug:slug>", views.index, name="category"),
    path('hakkimizda/', views.about, name="about")
]
