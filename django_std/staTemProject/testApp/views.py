from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    date = datetime.datetime.now()
    msg=None
    h = int(date.strftime('%H'))
    if h<12 :
        msg = "hello, very good morning"
    elif h<16 :
        msg = "hello , very good afterNoon"
    elif h<21 :
        msg = "hello , very good evening"
    else:
        msg = "hello , good night"
    my_dict = {"insert_date":date,"insert_msg":msg}
    return render(request,"wish.html",context=my_dict)