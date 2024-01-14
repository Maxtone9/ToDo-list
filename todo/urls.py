from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.todo_list, name='todo_list'),
    path('todos/add/', views.add_todo, name='add_todo'),
    path('todos/<int:todo_id>/toggle/', views.toggle_complete, name='toggle_complete'),
]
