from django.shortcuts import render
from django.views.generic import ListView
from .models import Yangilik

# Create your views here.
class Uy(ListView):
    model = Yangilik
    template_name='uy.html'
