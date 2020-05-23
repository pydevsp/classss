from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def time_view(request):
    time = datetime.datetime.now()
    return HttpResponse("<h2>hello current date and time : "+str(time)+"</h1>")

