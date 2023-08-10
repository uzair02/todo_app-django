from django.shortcuts import render

from todo.models import Task


def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('updated_at')
    cmpltd = Task.objects.filter(is_completed=True)
    #print(tasks)
    context = {
        'tasks': tasks,
        'cmpltd': cmpltd,
    }
    return render(request, 'home.html', context)