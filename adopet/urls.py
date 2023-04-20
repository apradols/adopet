from django.contrib import admin
from django.urls import path
from adopet.views import home

urlpatterns = [
    path('', home)
]
