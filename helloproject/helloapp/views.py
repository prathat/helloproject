from django.shortcuts import render
import re
from datetime import datetime
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, World! This is an http response from django`s webserver")
def page1(request):
    return HttpResponse("Hello, World! This is PAGE1")
def timepage(request,name):
    return render(request,'helloapp/timepage.html',{"name": name, "date": datetime.now()})
    
    
