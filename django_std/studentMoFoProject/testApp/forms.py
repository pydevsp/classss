from django import forms
from testApp.models import Student
# from django.db import models

class StudentForm(forms.ModelForm):
    # name = forms.CharField()
    def clean_marks(self):                     ####
        inputmarks = self.cleaned_data["marks"]
        if inputmarks <= 100 :
            pass
        else :
            raise forms.ValidationError("enter valid mark")
        return inputmarks
    class Meta :
        model = Student
        fields = "__all__"