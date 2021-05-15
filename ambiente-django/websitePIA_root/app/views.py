from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def page1(request):
    return render(request,"page1.html")

def page2(request):
    return render(request,"page2.html")

def page3(request):
    return render(request,"page3.html")

def page4(request):
    return render(request,"page4.html")

def estanteria1(request):
    return render(request,"estanteria1.html")

def estanteria2(request):
    return render(request,"estanteria2.html")

def estanteria3(request):
    return render(request,"estanteria3.html")

def estanteria4(request):
    return render(request,"estanteria4.html")