from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, "home.html")

def Opportunities(request):
    return render(request, "opportunities.html")
