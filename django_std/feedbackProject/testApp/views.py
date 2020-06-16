from django.shortcuts import render
from . import forms
# Create your views here.
def t_View(request):
    return render(request,"testapp/thanks.html")  ## old V
def feedbackView(request):
    if request.method == 'GET':
        form = forms.feedbackForm()
        

    if request.method == 'POST' :
        form = forms.feedbackForm(request.POST)
        if form.is_valid() :
            print("form validation success and printing data")
            print("student name :",form.cleaned_data['name'])    #### cleaned_data =====> alredy velidated
            print("student rollno :",form.cleaned_data['rollno'])
            print("student email :",form.cleaned_data['email'])
            print("student feeds :",form.cleaned_data['feedback'])
            # return t_View(request)  ## old V
            return render(request,"testapp/thanks.html",{"namo":form.cleaned_data['name']})
    return render(request,'testapp/feedback.html',{"form":form})