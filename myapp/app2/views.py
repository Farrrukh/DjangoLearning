from django.contrib import auth
from django.shortcuts import render, redirect


# Create your views here.



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        x=auth.authenticate(username=username,password=password)
        if x is not None:
            auth.login(request,x)
            return redirect('/')
        else:
            return redirect('login')
    else:
        return render(request,'login.html',)