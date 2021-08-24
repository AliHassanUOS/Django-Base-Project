from django import forms
from django import forms
from django.forms import widgets
from django.forms.fields import DateTimeField, IntegerField




class StudentForm(forms.Form):

    name = forms.CharField(widget = forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget = forms.EmailInput(attrs={"class": "form-control"}))
    number  = forms.IntegerField(widget = forms.NumberInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(widget= forms.PasswordInput(attrs={"class": "form-control"}))

        
    
    # def clean_name(self):

    #     name = self.cleaned_data["name"]

    #     if (name) == "ali":

    #         raise forms.ValidationError("Please enter name as ali")
        
    #     return name
    
    def clean(self):
        cleaned_data  = super().clean()

        pass1 = self.cleaned_data["password"]
        pass2 = self.cleaned_data["password1"]

        
        if len(pass1) < 4 :
            raise forms.ValidationError("Enter greater 4")
        
        if len(pass2) < 4 :
            raise forms.ValidationError("Enter greater 4")
        
        if pass1 != pass2:

            raise forms.ValidationError("Passowrd Does not match")









    







