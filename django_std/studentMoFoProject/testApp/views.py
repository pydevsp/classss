from django.shortcuts import render
from testApp import forms
# Create your views here.
def Student_views(request):
    form = forms.StudentForm()
    if request.method=="POST" :
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)   #### default value also True =====> form.save()
            print('form data inserted into database successfully')
    return render(request,'testapp/register.html',{'form':form})
