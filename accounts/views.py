from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confpassword']:
            try:
                user = User.objects.get(username=request.POST['username'])
                messages.error(request, 'Username already in use!')
                return render(request, 'accounts/signup.html')
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password'])
                auth.login(request,user)
                return redirect('home')
        else: 
            messages.error(request, 'Passwords must match!')
            return render(request, 'accounts/signup.html')
    else:
        return render(request, 'accounts/signup.html')    

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password incorrect!')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'products/home.html')
