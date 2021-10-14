from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html')

def ToDoApp(request):
    return HttpResponse("We're at To Do App Page.")
