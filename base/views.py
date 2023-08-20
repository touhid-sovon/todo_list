from django.shortcuts import render, redirect
from .models import *

from .forms import *
# Create your views here.

def home(request):
    tasks = Task.objects.all()
    
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}

    return render(request,'base/home.html',context)

def update_list(request,pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST' :
        form = TaskForm(request.POST, instance=task)
        if form.is_valid :
            form = form.save()
            return redirect('/')
    context = {'form': form}
    return render(request,'base/update_list.html',context) 

def delete_list(request,pk):
    task = Task.objects.get(id = pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'task':task}
    return render(request,'base/delete_list.html',context)



