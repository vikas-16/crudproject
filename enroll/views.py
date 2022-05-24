from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect
from .form import Studentregistration
from django.contrib.auth.hashers import make_password
from .form import *


def add_show(request):
    fm = Studentregistration()
    stud = User.objects.all()
    print(stud,'======================stud')
    if request.method == 'POST':
        fm = Studentregistration(request.POST,request.FILES)
        if fm.is_valid():
       
            tm =fm.cleaned_data['password']
            print(tm,'===========tm')
       
            test = fm.password = make_password(tm)
            #print(test,'=================fm.passwoerergergergrd = make_password(tm)')
       
            fm.save()
            fm = Studentregistration()
        else:
           pass
    return render(request, 'enroll/addandshow.html', {'form':fm,'stu':stud})   




def update_data(request, id):
    pi = User.objects.get(pk=id)
    if request.method == 'POST':
        fm = Studentregistration(request.POST,request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
    fm = Studentregistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form':fm})



def delete_data(request, id):
    if request.method == 'POST':
     pi = User.objects.get(pk=id)
     pi.delete()
     return HttpResponseRedirect('/')

