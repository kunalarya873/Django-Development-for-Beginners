from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from pytz import timezone

def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return HttpResponse("Contact Done!")
def reg(request):
    curr = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %I:%M:%S %p')
    if request.method == 'POST':
        emailID = request.POST['email']
        password = request.POST['psw']
        rep_password = request.POST['psw-repeat']
        print(emailID, password, rep_password)

    return render(request, 'reg.html', {'username': curr})