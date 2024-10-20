from django import forms
from .models import usersForm
from .models import UploadedFile

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import addPhone


class ExampleForm(forms.Form):
    name = forms.CharField(label='ชื่อ-นามสกุล', required=True , max_length=100)
    email = forms.EmailField(label='อีเมล์', required=True)
    rank = forms.CharField(label='ตำแหน่ง', required=True)
    work = forms.CharField(label='หน่วยงาน', required=True)
    work_number = forms.IntegerField(label='เบอร์โทรศัพท์ที่ทำงาน', required=True)
    phone_number = forms.IntegerField(label='เบอร์โทรศัพท์มือถือ', required=True)
  
class TopForm(forms.ModelForm):
    
    class Meta:
        model = usersForm
        fields = ["name","email","rank","work","work_number","phone_number"]
        

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file', 'text']

class BookingForm(forms.Form):
    eventTitle = forms.CharField(label="Event", max_length=255, required=True)
    startDateTime = forms.DateTimeField(label="Start Date and Time", input_formats=['%Y/%m/%d %H:%M'], required=True)
    endDateTime = forms.DateTimeField(label="End Date and Time", input_formats=['%Y/%m/%d %H:%M'], required=True)
    descript = forms.CharField(widget=forms.Textarea, required=True, label="Description")

class addRegister(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50) 
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username","first_name","last_name","password1","password2","email")

class phone(forms.ModelForm):
    phone = forms.CharField(max_length=10) 
    
    class Meta:
        model = addPhone
        fields = ["phone"]
