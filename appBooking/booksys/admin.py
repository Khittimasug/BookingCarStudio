from django.contrib import admin


# Register your models here.
from .models import User
from .models import Car
from .models import Booking

class MemberAdmin(admin.ModelAdmin):
    list_display="email","username","password","phone","is_staff","is_superuser","first_name","last_name"

admin.site.register(User)
admin.site.register(Car)
admin.site.register(Booking)
