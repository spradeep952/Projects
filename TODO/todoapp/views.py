from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task


def home(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}

    if request.method == 'POST':
        title = request.POST['title']
        task = Task.objects.create(title=title)
        task.save()
        return redirect('home')

    return render(request, 'main.html', context=context)

def modifyTask(request, pk):
    task = Task.objects.get(id=pk)
    context = {'task': task}
    return render(request, 'modify_task.html', context=context)