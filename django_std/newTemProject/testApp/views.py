from django.shortcuts import render
import testApp
# Create your views here.
def movieInfo(request):
    my_dict = {'head_msg':"MOVIES INFO",
        "sub_msg1": "SRK",
        'sub_msg2' : "ddlj",
        'sub_msg3': "don",
        'photo':'images/srk.jpg',
        }
    return render(request,'testApp/news.html',context=my_dict)    

def sportInfo(request):
    my_dict = {'head_msg':'SPORTS INFO',
        'sub_msg1':'ms dhoni',
        'sub_msg2':'csk',
        'sub_msg3':'india team captain'}
    return render(request,'testApp/news.html',context=my_dict)

def politicInfo(request):
    my_dict = {'head_msg':'BJD',
        'sub_msg1':'acche din',
        'sub_msg2':'abcd',
        'sub_msg3':'xyz',
        }
    return render(request,'testApp/news.html',context=my_dict)

def Index(request):
    return render(request,'testApp/index.html')