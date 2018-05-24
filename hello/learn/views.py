from django.shortcuts import render
from django.http import HttpResponse
def say_hello(request):
    return HttpResponse("Welcome to my github website")


# Create your views here.
