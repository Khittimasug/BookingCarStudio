from django.contrib import admin
from Test.models import users
from Test.models import usersForm
from Test.models import UploadedFile
from Test.models import Booking
# Register your models here.
admin.site.register(users)
admin.site.register(usersForm)
admin.site.register(UploadedFile)
admin.site.register(Booking)