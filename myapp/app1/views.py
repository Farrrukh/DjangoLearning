from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        firstName=request.POST['first_name']
        lastName=request.POST['last_name']
        email=request.POST['email_id']
        password=request.POST['password']

        x=User.objects.create_user(username=username,first_name=firstName,last_name=lastName,email=email,password=password)
        x.save()
        print('user created')
        return redirect('/')
    else:
        return render(request,'form.html')