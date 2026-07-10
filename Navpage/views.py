from django.shortcuts import render
from django.http import HttpResponse

# Home 
def home_view(request):
    return HttpResponse("<h1>This is home page</h1>")

# About 
def about_view(request):
    return HttpResponse("<h1>This is about page</h1>")