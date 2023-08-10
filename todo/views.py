from django.shortcuts import redirect, render
from .models import Task

def addTask(request):
    #print(request.POST['task'])
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')
