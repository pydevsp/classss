from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display (request):                  ###  request  ===> argument veriable 
    s = ("<h1 style= 'color:#f00fff'>welcome to django</h1>",
    "<h3>hiiiiihhh</h3>")
    return HttpResponse(s)      


def good_M(request):
    a = "<h1 style= 'color:#ff0fff'>good Morning </h1>"
    return HttpResponse(a)


def good_E(request):
    a = "<h1 style= 'color:#ff0fff'>good Evening  </h1>"
    return HttpResponse(a)    