from django.db import models 
from django.contrib.auth.models import UserManager,AbstractBaseUser,PermissionsMixin
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages
# Create your models here.

class CustomUserManager(UserManager):
    def _create_user(self, email,username, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        
        email = self.normalize_email(email)
        user = self.model(email=email,username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self,email=None,username=None,password=None,**extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email,username, password, **extra_fields)

    def create_superuser(self, email=None,username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email,username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default="")
    username = models.CharField(max_length=255, blank=True, default="",unique=True)
    first_name = models.CharField(max_length=255, blank=True, default="")
    last_name = models.CharField(max_length=255, blank=True, default="")

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    rank = models.IntegerField(default=1, blank=True, null=True)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "username" 
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def get_full_name(self):
        return self.first_name
    
    def get_short_name(self):
        return self.first_name or self.email.split("@"[0])
    
class Car(models.Model):
    file = models.ImageField(upload_to='uploads/')
    car_type = models.CharField(max_length=255, blank=True, default="",null=True)
    car_system = models.CharField(max_length=255, blank=True, default="",null=True)
    car_seat = models.IntegerField(blank=True, null=True)

class UploadedFile(models.Model):
    file = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_approve = models.BooleanField(default=False)

class PDFUpload(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_approve = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Booking(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    car = models.ForeignKey(Car,blank=True, null=True, on_delete=models.CASCADE)
    pdf = models.ForeignKey(PDFUpload,blank=True, null=True, on_delete=models.CASCADE)
    eventTitle = models.CharField(max_length=255)
    startDateTime = models.DateTimeField(null=True, blank=True , default=timezone.now()) 
    endDateTime = models.DateTimeField(null=True, blank=True , default=timezone.now())
    descript = models.TextField(blank=True)
    
    def save(self,*args,**kwargs):
        self.startDateTime = self.startDateTime + timedelta(hours=7)
        self.endDateTime = self.endDateTime + timedelta(hours=7)
        return super().save(*args, **kwargs)
    
    def clean(self):

        overlapping_bookings = Booking.objects.filter(
            car=self.car,
            startDateTime__lt=self.endDateTime, 
            endDateTime__gt=self.startDateTime  
        ).exclude(pk=self.pk).exists()

        if overlapping_bookings:
            raise messages("The selected car is already booked for the specified time period.")

    def __str__(self):
        return self.eventTitle
