from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from pytz import timezone
from .models import Student, Profile

def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    fullName = 'Ravi Kumar'
    c_id = 502
    age = 21
    s = Student(name= fullName, collegeID= c_id, age= age)
    s.save()
    print("Done")
    return render(request, 'contact.html')

def reg(request):
    curr = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %I:%M:%S %p')
    if request.method == 'POST':
        emailID = request.POST['email']
        password = request.POST['psw']
        rep_password = request.POST['psw-repeat']
        print(emailID, password, rep_password)

        if password == rep_password:
            s = Profile(email = emailID, pasw= rep_password)
            s.save()
            return redirect('/contact')
        else:
            return redirect('/reg')

    return render(request, 'reg.html', {'username': curr})
