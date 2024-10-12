from django import forms
from .models import usersForm
from .models import UploadedFile

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
