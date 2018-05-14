from django.shortcuts import render

# Create your views here.

#from djangoproject: https://docs.djangoproject.com/en/2.0/intro/tutorial01/
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. Welcome to the database.")