from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect
from .form import Studentregistration
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from .form import *
# Create your views here.

########## This Function show add item###############

def add_show(request):
    fm = Studentregistration()
    stud = User.objects.all()
    if request.method == 'POST':
        fm = Studentregistration(request.POST)
        if fm.is_valid():
       
            tm =fm.cleaned_data['password']
            print(tm,'===========tm')
        #  rgm = User(name=cm, email=gm, password=tm)
        #  rgm.save()
            test = fm.password = make_password(tm)
            print(test,'=================fm.passwoerergergergrd = make_password(tm)')
        # fm.make_password(fm.tm)
            fm.save()
            fm = Studentregistration()
        else:
           pass
    return render(request, 'enroll/addandshow.html', {'form':fm,'stu':stud})   

#########THIS DELETE FUNCTION###########
def delete_data(request, id):
    if request.method == 'POST':
     pi = User.objects.get(pk=id)
     pi.delete()
     return HttpResponseRedirect('/')

