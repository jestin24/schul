from django.shortcuts import render
from django.shortcuts import render, redirect

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def log(request):
    return render(request,'log.html')

# Create your views here.
def register(request):
    return render(request,'register.html')

def reg(request):
    return render(request,'registerform.html')
def wel(request):
    return render(request,'wel.html')
def sub(request):
    return render(request,'sub.html')