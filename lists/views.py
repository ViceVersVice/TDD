from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def SomeView(request):
    return HttpResponse("<html><title>To-Do</title></html>")