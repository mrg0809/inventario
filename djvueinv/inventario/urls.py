from django.shortcuts import render
from django.urls import path
from . import views

def index(request):
    context = {}

    return render(request, 'index/index.html', context)

urlpatterns = [
    path('', views.index, name='index'),
]