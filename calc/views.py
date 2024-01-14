from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def  home(request):
    return render(request,'index.html',{'name':"Febin"})

def add(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    result = int(val1)+int(val2)

    return render(request,'add.html',{'result':result})