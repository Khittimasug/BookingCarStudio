from django.contrib import admin
from Test.models import users
from Test.models import usersForm
from Test.models import UploadedFile
from Test.models import Booking

from Test.models import addPhone
from Test.models import carBooking
from Test.models import car
from Test.models import PDFUpload
# Register your models here.
admin.site.register(users)
admin.site.register(usersForm)
admin.site.register(UploadedFile)
admin.site.register(Booking)
admin.site.register(addPhone)
admin.site.register(car)
admin.site.register(carBooking)
admin.site.register(PDFUpload)

