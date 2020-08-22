from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("users/", views.users, name="users"),
    path('help/', views.help, name='help'),

]
