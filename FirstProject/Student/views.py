from django.http import HttpResponse
from django.shortcuts import render
from  FirstProject.models import Profile

# Create your views here.
def home(request):
    p = Profile.objects.all()
    return render(request, 'check.html', {'data': p})

