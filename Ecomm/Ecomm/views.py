from django.shortcuts import render, redirect
from . models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def home(request):
    return render(request, "index.html")
def main(request):
    return render(request, 'main.html')
def login_call(request):
    if request.method == 'POST':
        username = request.POST['uname']
        psw = request.POST['psw']
        currUser = authenticate(username= username, password = psw)
        if currUser:
            login(request, currUser)
            return main(request)
        else:
            return redirect('signup/')
        print(username, psw)
    return render(request, 'loginpage.html')
def logout_call(request):
    logout(request)
    return redirect('/login')
def signup(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        mobile = request.POST['mobile']
        email = request.POST["email"]
        psw = request.POST['psw']
        psw_repeat = request.POST['psw-repeat']
        u =User(first_name = fullname, username= email,email= email, password = psw_repeat)
        u.save()
        p = Profile(user = u, mobile= mobile)
        p.save()
        print("Data Saved")
        return redirect('/login')
    return render(request, 'register.html')
