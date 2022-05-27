from django.db import models

class Student(models.Model):
    name          = models.CharField(max_length=70)
    email         = models.CharField(max_length=70)
    password      = models.CharField(max_length=70)
    upload        = models.ImageField(upload_to='media',blank=True)

    
       