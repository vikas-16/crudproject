from django.shortcuts import render
from .form import Studentregistration
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from .form import *
# Create your views here.

def add_show(request):
    fm = Studentregistration()
    stud = User.objects.all()
    if request.method == 'POST':
        fm = Studentregistration(request.POST)
        if fm.is_valid():
        #  cm =fm.cleaned_data['name']
        #  gm =fm.cleaned_data['email']
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
    return render(request, 'enroll/addandshow.html', {'form':fm,'stu':stud})    

