from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib import messages
# Create your views here.
def username_present(username):
    if User.objects.filter(username=username).exists():
        return True
    else:
        return False

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        username_pre = username_present(username=username)
        email = request.POST.get('email')
        password = request.POST.get('passoword')
        if username_pre:
            messages.error(request, f"The User Name {username} exists")
            return redirect('/signup')
        else:
            user1 = User.objects.create_user(username, email, password)
            user1.save()
            auth.login(request, user=user1)
            return redirect('/')
    else:
        return HttpResponse("Page Not Found")

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user=user)
            messages.success(request, "Successfully Logged In")
            return redirect('/')
        else:
            messages.success(request, "Invalid Credentials")
            return redirect('/')
    else:
        return HttpResponse("Page Not Found")

def logout(request):
    auth.logout(request)
    return redirect('/')