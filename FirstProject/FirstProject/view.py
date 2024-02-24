from django.http import HttpResponse
def home(request):
    return HttpResponse("Done!")
def contact(request):
    return HttpResponse("Contact Done!")