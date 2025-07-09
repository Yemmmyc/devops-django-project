from django.shortcuts import render
from django.http import HttpResponse

def hello_view(request):
    return HttpResponse("Hello DevOps!")

def home_view(request):
    return render(request, 'hello/home.html')
