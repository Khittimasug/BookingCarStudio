from django.db import models
from datetime import datetime, timedelta
from django.db import models
from django.utils.timezone import localtime

from django.contrib.auth.models import User

# Create your models here.
class users(models.Model):
    name = models.CharField( max_length=500)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    
    def __str__(self):
        return self.name
    
class usersForm(models.Model):
    name = models.CharField( max_length=500)
    email = models.EmailField(max_length=255, unique=True)
    rank = models.CharField(max_length=255)
    work = models.CharField(max_length=255)
    work_number = models.IntegerField()
    phone_number = models.IntegerField()
    
    def __str__(self):
        return self.name
    

class UploadedFile(models.Model):
    file = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(null=True, max_length=500)

class Booking(models.Model):
    eventTitle = models.CharField(max_length=255)
    startDateTime = models.DateTimeField(null=True, blank=True) 
    endDateTime = models.DateTimeField(null=True, blank=True)
    descript = models.TextField(blank=True)
    
    def save(self,*args,**kwargs):
        self.startDateTime = self.startDateTime + timedelta(hours=7)
        self.endDateTime = self.endDateTime + timedelta(hours=7)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.eventTitle

class addPhone(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="userKey")
    phone = models.CharField(max_length=10)

class car(models.Model):
    car_file = models.ImageField(upload_to='uploads/')
    car_name = models.CharField(max_length=255)
    car_id = models.CharField(max_length=255)
    type_car = models.CharField(max_length=255)
    seat = models.IntegerField()
    color = models.CharField(max_length=255)
    #startDateTime = models.DateTimeField(null=True, blank=True) 
    #endDateTime = models.DateTimeField(null=True, blank=True)

class carBooking(models.Model):
    car_name = models.CharField(max_length=255)
    car_id = models.CharField(max_length=255)
    startDateTime = models.DateTimeField(null=True, blank=True) 
    endDateTime = models.DateTimeField(null=True, blank=True)
    type_car = models.CharField(max_length=255)
    seat = models.IntegerField()
    color = models.CharField(max_length=255)

class PDFUpload(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
