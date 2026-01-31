from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,logout
from django.contrib.auth.models import User


# Create your views here.
def login_(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        u = authenticate(username=username,password=password)
        if u is not None:
            return redirect ('home')
        else:
            return HttpResponse('wrong creditals')
    return render(request,'login.html')
        
def register_(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        U = User.objects.create(username=username,password=password)
        U.set_password(password)
        U.save()
        return redirect('login')
    return render(request,'register.html')

def logout_(request):
    logout(request)
    return redirect('login')