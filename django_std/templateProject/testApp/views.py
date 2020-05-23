from django.shortcuts import render
import datetime
# Create your views here.
def wishTo(request):
    # return render(request,'testApp/wish.html')   ###########4
    date = datetime.datetime.now()
    my_dict = {"insert_date":date}
    return render(request, 'testApp/wish.html',context=my_dict)

def std_temp(request):
    dt = datetime.datetime.now()
    name ="ABC"
    rollno = "R101"
    mark = 80
    my_dictt = {"date":dt,"name":name,"rollno":rollno,"marks":mark}
    return render(request,"testApp/results.html" , context=my_dictt)



def good_msg(request):
    da =datetime.datetime.now()
    msg = "hello ,very very good"
    h = int(da.strftime("%H"))
    if h<12:
        msg +='morning !!!'
    elif h<16:
        msg +="afrNoon"
    elif h<21:
        msg +="evening "
    else :
        msg += "night"

    my_dict = {'insert_date':da,"insert_msg":msg}
    return render(request,"testApp/good.html" , context=my_dict)
