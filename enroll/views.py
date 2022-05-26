from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect, redirect
from .form import Studentregistration
from django.contrib.auth.hashers import make_password
from .form import *
from cryptography.fernet import Fernet
from django.http import HttpResponse
from .encrypt_util import encrypt,decrypt
from django.contrib import messages

def view_data(request):
    stud = Student.objects.all()
    return render(request, 'enroll/view.html', {'stu':stud})


def add_show(request):
    fm = Studentregistration()
    stud = Student.objects.all()
   
    if request.method == 'POST':
        fm = Studentregistration(request.POST,request.FILES)
       
        if fm.is_valid():
            password = fm.cleaned_data['password']
            encryptpass= encrypt(['password'])
           
            fm.save()
            fm = Studentregistration()
            messages.success(request, 'Succes form.')
            return render(request, 'enroll/view.html', {'form':fm,'stu':stud})
        
        else:
           pass
    return render(request, 'enroll/addandshow.html', {'form':fm})   




def update_data(request, id):
    pi = Student.objects.get(pk=id)
    if request.method == 'POST':
        fm = Studentregistration(request.POST,request.FILES, instance=pi)
        if fm.is_valid():
            messages.success(request, 'Update successfully.')
            fm.save()
   
    fm = Studentregistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form':fm})



def delete_data(request, id):
    if request.method == 'POST':
     pi = Student.objects.get(pk=id)
     pi.delete()
    messages.success(request, 'Delete successfully.')
    return redirect('view_data')