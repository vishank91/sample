from .models import Employee
from django import forms
from django.contrib.auth.models import User
class Employee_Form(forms.ModelForm):
    id=forms.CharField(widget=forms.NumberInput(attrs={'class':'form_control','placeholder':'Enter Employee Id'})
                       ,required=True,max_length=10)
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form_control','placeholder':'Enter Employee Name'})
        ,required=True, max_length=20)
    dsg = forms.CharField(widget=forms.TextInput(attrs={'class':'form_control','placeholder':'Enter Designation'})
                          , required=True, max_length=20)
    salary = forms.CharField(widget=forms.NumberInput(attrs={'class':'form_control','placeholder':'Enter Salary'})
                             , required=True, max_length=10)
    class Meta():
        model=Employee
        fields=('id','name','dsg','salary')

'''
class userform(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(),required=True,max_length=20)
    email = forms.CharField(widget=forms.EmailInput(), required=True, max_length=20)
    first_name = forms.CharField(widget=forms.TextInput(), required=True, max_length=20)
    last_name = forms.CharField(widget=forms.TextInput(), required=True, max_length=20)
    password = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=20)
    class Meta():
        model=User
        feilds=__all__

'''