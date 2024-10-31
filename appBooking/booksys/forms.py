from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import User
from .models import Car
from .models import UploadedFile
from .models import Booking
from django.core.exceptions import ValidationError
from .models import PDFUpload


class addRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","first_name","last_name","password1","password2","email","phone")

class addCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['file','car_type','car_system','car_seat']

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']

class BookingForm(forms.Form):
    eventTitle = forms.CharField(label="Event", max_length=255, required=True)
    startDateTime = forms.DateTimeField(label="Start Date and Time", input_formats=['%Y/%m/%d %H:%M'], required=True)
    endDateTime = forms.DateTimeField(label="End Date and Time", input_formats=['%Y/%m/%d %H:%M'], required=True)
    descript = forms.CharField(widget=forms.Textarea, required=True, label="Description")

    def clean(self):
        cleaned_data = super().clean()
        startDateTime = cleaned_data.get("startDateTime")
        endDateTime = cleaned_data.get("endDateTime")

        if startDateTime and endDateTime:
            # ตรวจสอบการจองซ้ำกัน
            overlapping_bookings = Booking.objects.filter(
                startDateTime__lt=endDateTime,
                endDateTime__gt=startDateTime
            ).exists()

            if overlapping_bookings:
                raise ValidationError("The selected car is already booked for the specified time period.")
                
        return cleaned_data
    
class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = PDFUpload
        fields = ['title', 'pdf_file']
    
    