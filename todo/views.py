# from django.shortcuts import render
# from django.http import HttpResponse
# from todo.models import *
# # Create your views here.
# def todo(request):
#     return render(request,'todo_home.html')

# def add(request):
#     if request.method == 'GET':
#         print(request.GET.get('title'))
#         return  HttpResponse("ADDED")

from django.shortcuts import render, redirect
from .models import TodoItem

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        TodoItem.objects.create(title=title)
        return redirect('todo_list')
    return render(request, 'add_todo.html')

def toggle_complete(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')


