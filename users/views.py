
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


# Create your views here.

def home(request):
    return render(request, "home.html")

