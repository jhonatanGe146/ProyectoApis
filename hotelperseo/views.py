from django.http import HttpResponse
from django.shortcuts import render

# def home(request):
#     return HttpResponse('<h2>ADSO Soacha los mejores desarrolladores</h2>')

def home(request):
    return render(request,'home.html')