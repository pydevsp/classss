from django.shortcuts import render

from django.http import HttpResponse




# Create your views here.
def first_view(request):
    return HttpResponse('<h1>Responce from 1st view </h1>')

def second_view(request):
    return HttpResponse('<h1>Responce from 2nd view </h1>')

def third_view(request):
    return HttpResponse('<h1>Responce from 3rd view </h1>')

def fourth_view(request):
    return HttpResponse('<h1>Responce from 4th view </h1>')