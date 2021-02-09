from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render(request,'index.html',{'titles':'farrukh khan'})

def expression(request):
    a=request.GET['text1']
    b=request.GET['text2']
    c=int(a)+int(b)
    return render(request,'output.html',{'result':c})

