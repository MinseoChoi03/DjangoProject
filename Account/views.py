from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == "post":
        if request.post["password1"] == request.post["password2"]:
            user = User.objects.create_user(
                username=request.post["username"], password=request.post["password1"])
            auth.login(request, user)
            return redirect('home')
        return render(request, 'Account/SignUp.html')

    return render(request, 'Account/SignUp.html')


def login(request):
    if request.method == "post":
        username = request.post['username']
        password = request.post['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'Account/login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'Account/login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
