from django.shortcuts import render, redirect
from .models import Task
from django_htmx.http import HttpResponseClientRefresh

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
    return HttpResponseClientRefresh()

def update_task(request, id):
    print('checkbox clicked')
    print('the id is', id)
    Task.objects.filter(id=id).update(is_completed=True) # filter and update
    return HttpResponseClientRefresh()

def delete_task(request, id):
    Task.objects.filter(id=id).delete() # filter and delete
    return HttpResponseClientRefresh()
    