from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"hello/index.html")


def showname(request):
    return HttpResponse("  Hello,Abu")


def greet1(request,name):
    return HttpResponse(f"hello,{name.capitalize()}")


def greet(request,name):
    return render(request,"hello/greet.html",{
        "name":name.capitalize()
    })


