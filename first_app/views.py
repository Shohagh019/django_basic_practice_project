from django.shortcuts import render
from django.http import HttpResponse

def courses(request):
    return HttpResponse("This is courses page")

def about(request):
    return HttpResponse("This is about page")
def first(request):
    return HttpResponse("This is first_app page")
