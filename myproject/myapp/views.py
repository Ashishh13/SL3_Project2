from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welome to my Django App!</h1>")

# Create your views here.
