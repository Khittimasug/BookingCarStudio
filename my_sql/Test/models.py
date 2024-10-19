from django.db import models


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
