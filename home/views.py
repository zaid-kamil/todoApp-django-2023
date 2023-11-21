from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def index(request):
    context = {
        'task_list' : Task.objects.all()
    }
    return render(request, 'index.html', context)

def add_task(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        if len(task) >= 2:
            Task.objects.create(title=task)
    redirect('home')

def update_task(request, id):
    context = {}
    return render(request, 'todo_list.html', context)

def delete_task(request, id):
    pass
    