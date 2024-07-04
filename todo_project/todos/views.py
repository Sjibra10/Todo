from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todos/index.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()
    return render(request, 'todos/add_todo.html', {'form': form})

def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/update_todo.html', {'form': form})
