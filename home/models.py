from distutils.command.upload import upload
#from django import forms 
from django.db import models


# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    desc = models.TextField()

    def __str__(self):
        return self.name+"-"+self.email

# class form(models.Model):
#     email = models.EmailField()
#     formFile = models.CharField(max_length=30)
#     file = models.FileField()

#     def __str__(self):
#         return self.email



