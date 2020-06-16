from django import forms
from django.core import validators     ## implicit validater ==== django inbuild 

def email_val(value):
    if value[len(value)-9 :] != "gmail.com" :
        raise forms.ValidationError("must be gmail")
def only_alpha (v):
    if v.isalpha() != True:
        raise forms.ValidationError("only alphabet ")

class feedbackForm(forms.Form):
    name = forms.CharField(validators=[only_alpha])
    rollno = forms.IntegerField(label="Roll No.")
    email = forms.EmailField(validators=[email_val])
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(label="password(again)" , widget=forms.PasswordInput)
    feedback = forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(100),
    validators.MinLengthValidator(10)])
    bot_handler = forms.CharField(required=False , widget= forms.HiddenInput)

        #### explicit validater ===== manual create 
    def clean_name(self):                        ####
        input = self.cleaned_data['name']
        if len(input) < 4 :
            raise forms.ValidationError("the min characters  should be 4")
        return input
    def clean_p(self):
        inpswd = self.cleaned_data['password']
        inrepswd = self.cleaned_data['repassword']
        if inpswd != inrepswd :
            raise forms.ValidationError("password not match")

    def clean(self):
        print("bot_validation")
        cleaned_data = super().clean()
        bot_handler_value = cleaned_data['bot_handler']
        if len(bot_handler_value) > 0 :
            raise forms.ValidationError("thanks bot") 
    # def clean_rollno(self):                     ####
    #     inputRollno = self.cleaned_data["rollno"]
    #     if len(str(inputRollno)) == 3 :
    #         pass
    #     else :
    #         raise forms.ValidationError("enter valid rollno")
    #     return inputRollno

    # def clean_feedback(self):                  ####
    #     inputfeed = self.cleaned_data["feedback"]
    #     if len(inputfeed)<25 :
    #         raise forms.ValidationError("atleast 25 characters")
    #     return inputfeed    