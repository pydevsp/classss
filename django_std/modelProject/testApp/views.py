from django.shortcuts import render
from testApp.models import Employee
import testApp

# Create your views here.

def empdata(request):
    emp_list = Employee.objects.all()
    print(emp_list)
    my_dict = {'emp_list':emp_list}
    return render(request,'testApp/emp.html',context=my_dict)