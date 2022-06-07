import email
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect, redirect
from .form import Studentregistration
from django.contrib.auth.hashers import make_password
from .form import *
from cryptography.fernet import Fernet
from django.http import HttpResponse
from .encrypt_util import encrypt,decrypt
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .token import *
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage  
from django.utils.encoding import force_text
from django.contrib.auth import login, authenticate  # add to imports
# authentication/views.py
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login




def home1(request):
    return render(request,'enroll/home.html')

# def Login(request):
#     pass
    # return render(request,'enroll/login.html')




# def login(request):
#     if request.user.is_authenticated:
#         return redirect('/books')
     
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username =username, password = password)
 
#         if user is not None:
#             login(request,user)
#             return redirect('/books')
#         else:
#             form = AuthenticationForm()
#             return render(request,'enroll/login.html',{'form':form})
     
#     else:
#         form = AuthenticationForm()
#         return render(request, 'enroll/success.html', {'form':form})


def login_request(request):
    User = get_user_model()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
         
            if user is not None:
               
                login(request, user)
                messages.error(request,"Invalid username or password.")
                return HttpResponse(f'Hello {user.username}! You have been logged in')
     
            else:
                 messages.error(request,"Invalid username or password.")
        else:
             messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="enroll/login.html", context={"login_form":form})




# def login(request):
#     message = ''
#     if request.method == 'POST':
#         print('===========')
#         form = LoginForm(request.POST)
#         print(form.is_valid(),"========================rtrtn")
#         if form.is_valid():
#             print(form.is_valid())
#             print(form.cleaned_data['username'],form.cleaned_data['password'],)
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
               
#             )
#             print(user,"========================user")
#             print(form.cleaned_data['username'],form.cleaned_data['password'],"=============================")
#             if user is not None:
#                 print(user,'============user')
#                 login(request, user)
#                 return HttpResponse(f'Hello {user.username}! You have been logged in')
#             else:
#                 message = 'Login failed!'
#     else:
#         form = LoginForm()
#     return render(
#         request, 'enroll/login.html', context={'form': form, 'message': message})


# def login(request):
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     user = authenticate(username = username, password = password)      

#     if user is not None:
#         login(request, user)
#         return HttpResponseRedirect('enroll/login.html')
#     else:
#         return HttpResponseRedirect('/enroll/login.html')
#     return render(request, 'enroll/login.html', {'form':form, 'title':'log in'})


# def signup(request):
#     User = get_user_model()
#     #print(User,"===============user")
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         print(form.is_valid(),form.errors,"++++++++++++++++++++++++++=")
#         if form.is_valid():
           
#             email = form.cleaned_data.get('email') 
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             messages.success(request, 'Delete successfully.')
#             current_site = get_current_site(request)
#             mail_subject = 'Activate your account.'
#             message = render_to_string('enroll/register_view.html', {
#                         'user': user,
#                         'domain': current_site.domain,
#                         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                         'token': account_activation_token.make_token(user),
#                     })
#             to_email = form.cleaned_data.get('email')
#             # print(to_email)
           
#             email = EmailMessage(  
#                         mail_subject, message, to=[to_email]  
#                   )
#             email.send()  
#             messages.success(request,'Please confirm your email address to complete the registration')
#             # return HttpResponse('Please confirm your email address to complete the registration')
#             return redirect('/user/login/')
           
#     else:
#         form = SignupForm()
#     return render(request, 'enroll/registration.html', {'form': form})
    
def signup(request):  
    if request.method == 'POST':  
        form = SignupForm(request.POST)  
        if form.is_valid():  
            # save form in the memory not in database  
            user = form.save(commit=False)  
            user.is_active = False  
            user.save()  
            # to get the domain of the current site  
            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('enroll/register_view.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()  
            return HttpResponse('Please confirm your email address to complete the registration')  
    else:  
        form = SignupForm()  
    return render(request, 'enroll/registration.html', {'form': form})  



def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        print(user,"====================user")
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
       
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        # print(user.is_active,"=============================")
        user.save()
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return HttpResponseRedirect('/user/login/')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        messages.success(request, 'Inavlid account.')
        return HttpResponseRedirect('/user/register/')

def success(request):
    return render(request, 'enroll/success.html')
    
def token_send(request):
    return render(request, 'enroll/token_send.html')    

def view_data(request):
  
    name = request.GET.get('name', None)
  
    if name:
      stud = Student.objects.filter(Q(name__icontains=name) | Q(email__icontains=name) | Q(password__icontains=name)) 
      
    else:
      
        stud = Student.objects.all()
        #messages.success(request, 'Not find any matching.')
    return render(request, 'enroll/view.html', {'stu':stud})



def add_show(request):
    fm = Studentregistration()
   
    stud =  Student.objects.all()
    print(stud,"++++++++++++++++++test")
   
    if request.method == 'POST':
        fm = Studentregistration(request.POST,request.FILES)
       
        if fm.is_valid():
            password = fm.cleaned_data['password']
            encryptpass= encrypt(['password'])
           
            fm.save()
           
            fm = Studentregistration()
            messages.success(request, 'Succes form.')
            return render(request, 'enroll/view.html', {'stu':stud,})
        
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