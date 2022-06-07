from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  
from .models import *
 

class Studentregistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','password','upload']
        
        widgets= {
            'name': forms.TextInput(attrs={'class':'form-control', 'autocomplete':'off'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'autocomplete':'off'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control', 'autocomplete':'off'}),
            }



class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        widgets= {
            'username': forms.TextInput(attrs={'class':'form-control', 'autocomplete':'off'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'autocomplete':'off'}),
            'password1': forms.PasswordInput(render_value=True, attrs={'class':'form-control', 'autocomplete':'off'}),
            'password2': forms.PasswordInput(render_value=True, attrs={'class':'form-control', 'autocomplete':'off'}),

            }



class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    widgets= {
            # 'username': forms.TextInput(attrs={'class':'form-control', 'autocomplete':'off'}),
            'username': forms.TextInput(attrs={'class':'form-control', 'autocomplete':'off'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control', 'autocomplete':'off'}),
            # 'password2': forms.PasswordInput(render_value=True, attrs={'class':'form-control', 'autocomplete':'off'}),

    }    