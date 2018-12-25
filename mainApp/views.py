from django.shortcuts import render
from .models import Employee
from .forms import Employee_Form
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse,HttpResponseRedirect
def home(request):
    data=Employee.objects.all()
    return render(request,"index.html",{'Data':data})

def details(request,num):
    data=Employee.objects.get(id=num)
    return render(request,"details.html",{'Data':data})

def add_Employee(request):
    if request.method=='POST':
        form=Employee_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_Employee/')
    else:
        form=Employee_Form()
    return render(request,'add_Employee.html',{'form':form})
'''
def registration(request):
    if request.method=='POST':
        form=userform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            return HttpResponseRedirect('/registration/')
    else:
        form=userform()
    return render(request,'reqistration.html',{'form':form})
'''

def registration(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/registration/')
    else:
        form=UserCreationForm()
    return render(request,'registration.html',{'form':form})