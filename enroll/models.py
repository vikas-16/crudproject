from django.db import models
from django.contrib.auth.models import User  

class Student(models.Model):
    user          = models.ForeignKey(User, on_delete=models.CASCADE)
    name          = models.CharField(max_length=70)
    email         = models.CharField(max_length=70)
    password      = models.CharField(max_length=70)
    upload        = models.ImageField(upload_to='media',blank=True)
    
    
       