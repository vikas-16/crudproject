from django import forms

from .models import *

class Studentregistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password','upload']

        widgets= {
            'name': forms.TextInput(attrs={'class':'form-control', 'autocomplete':'off'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'autocomplete':'off'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control', 'autocomplete':'off'}),
            }


