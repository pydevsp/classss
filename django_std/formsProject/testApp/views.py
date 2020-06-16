from django.shortcuts import render
from . import forms                       #######    from . means current working directory


# Create your views here.
def StudentRegisterview(request):
    form = forms.StudentRegister()
    # if request.method == "POST":
    #     form = forms.StudentRegister(request.POST)
    #     if form.is_valid():
    #         print("form val succ")
    #         print("Name:",form.cleaned_data["name"])
    #         print("Mark :",form.cleaned_data["marks"])
    my_dict = {'form':form}
    return render(request,'testApp/register.html',context=my_dict)
