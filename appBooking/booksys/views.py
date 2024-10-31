from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import get_object_or_404, redirect
from .forms import addRegister,addCarForm,BookingForm, FileUploadForm, PDFUploadForm

from .models import User
from .models import Car,PDFUpload
from datetime import timedelta
from django.utils.timezone import localtime
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from django.views.generic import FormView
from django.core.serializers.json import DjangoJSONEncoder
import pytz
import json

from .models import Booking

TIMEZONE = "Asia/Bangkok"

SCOPES = ["https://www.googleapis.com/auth/calendar"]
calendarId = ("c_8aad91cf2490fc5903dde7745e60a4315f4618937af23310b9ee0fbeb6820a8a@group.calendar.google.com")

def home(request):
    return render(request ,"home.html")

def register_view(request):
    if request.method == "POST":
        form3 = addRegister(request.POST)
        if form3.is_valid():
            user = form3.save()
            login(request, user)
            return redirect("dashboard")
    else:
        initial_data = {
                "first_name": "",
                "last_name": "",
                "email": "",
                "username": "",
                "password1": "",
                "password2": "",
                "phone": "",
        }
        form3 = addRegister(initial=initial_data)
    return render(request, "auth/register.html", {"form3": form3})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid() and User.objects.get(username=request.POST["username"]).is_superuser:
            user = form.get_user()
            login(request, user)
            return redirect("/adminDashboard")
        elif form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
        
    else:
        initial_data = {"username": "", "password1": ""}
        form = AuthenticationForm(initial=initial_data)
    return render(request, "auth/login.html", {"form": form})


def dashboard_view(request):
    print(request.user)
    allBook = Booking.objects.all()
    for i in allBook:
        print(i.user)
        if i.user == request.user:
            print("Yes")
            bookings = Booking.objects.get(user=request.user.id)
            return render(request, "dashboard.html",{"bookings": bookings,"BoolX": False})
    return render(request, "dashboard.html",{"BoolX": False})


def logout_view(request):
    logout(request)
    return redirect("login")

def adminDashboard_view(request):
    return render(request, "adminDashboard.html")

def updateProfile(request, id):
    user = User.objects.get(id=id)
    return render(request, "updateProfile.html", {"user": user})

def uprecProfile(request, id):
    user = get_object_or_404(User, id=id)
    
    user.email = request.POST.get("email")
    user.username = request.POST.get("username")
    password = request.POST.get("password")
    if password:
        user.set_password(password)  
    user.first_name = request.POST.get("first_name")
    user.last_name = request.POST.get("last_name")
    user.phone = request.POST.get("phone")

    user.save()
    update_session_auth_hash(request, user) 

    return redirect("/dashboard")

@user_passes_test(lambda user: user.is_superuser)
def adminDash(request):
    user = User.objects.all()
    context = {"user": user}
    return render(request, "adminUserEdit.html", context)
@user_passes_test(lambda user: user.is_superuser)
def add(request):
    return render(request, "add.html")

@user_passes_test(lambda user: user.is_superuser)
def addrec(request):
    try:
        if User.objects.get(username=request.POST["username"]):
            print("Yo")
    except ObjectDoesNotExist:
        rank = request.POST["rank"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        phone = request.POST["phone"]
        #is_staff = request.POST["is_staff"]
        #is_superuser = request.POST["is_superuser"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        user = User(
            rank=rank,
            email=email,
            username=username,
            password=password,
            phone=phone,
            #is_staff=is_staff,
            #is_superuser=is_superuser,
            first_name=first_name,
            last_name=last_name,
        )
        user.save()
    return redirect("/adminEditUser")

@user_passes_test(lambda user: user.is_superuser)
def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect("/adminEditUser")

@user_passes_test(lambda user: user.is_superuser)
def update(request, id):
    user = User.objects.get(id=id)
    return render(request, "update.html", {"user": user})

@user_passes_test(lambda user: user.is_superuser)
def uprec(request, id):
    rank = request.POST["rank"]
    email = request.POST["email"]
    username = request.POST["username"]
    password = request.POST["password"]
    phone = request.POST["phone"]
    #is_staff = request.POST["is_staff"]
    #is_superuser = request.POST["is_superuser"]
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]

    user = User.objects.get(id=id)
    user.rank = rank
    user.email = email
    user.username = username
    user.set_password(password)
    print("Set")
    user.phone = phone
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    return redirect("/adminEditUser")

@user_passes_test(lambda user: user.is_superuser)
def adminDashCar(request):
    car = Car.objects.all()
    context = {"car": car}
    return render(request, "adminCarEdit.html", context)
@user_passes_test(lambda user: user.is_superuser)
def addCar(request):
    form = addCarForm()
    return render(request, "addCar.html" , {"form": form})
@user_passes_test(lambda user: user.is_superuser)
def addrecCar(request):
    file = request.FILES["file"]
    car_type = request.POST["car_type"]
    car_system = request.POST["car_system"]
    car_seat = request.POST["car_seat"]
    car = Car(
        file=file,
        car_type=car_type,
        car_system=car_system,
        car_seat=car_seat,
    )
    car.save()
    return redirect("/adminEditCar")

@user_passes_test(lambda user: user.is_superuser)
def deleteCar(request, id):
    car = Car.objects.get(id=id)
    car.delete()
    return redirect("/adminEditCar")

@user_passes_test(lambda user: user.is_superuser)
def updateCar(request, id):
    form = addCarForm()
    car = Car.objects.get(id=id)
    return render(request, "updateCar.html", {"car": car,"form": form})

@user_passes_test(lambda user: user.is_superuser)
def uprecCar(request, id):
    file = request.FILES["file"]
    car_type = request.POST["car_type"]
    car_system = request.POST["car_system"]
    car_seat = request.POST["car_seat"]

    car = Car.objects.get(id=id)
    car.file = file
    car.car_type = car_type
    car.car_system = car_system
    car.car_seat = car_seat
    car.save()
    return redirect("/adminEditCar")

def build_service(request):
    credentials = service_account.Credentials.from_service_account_file(('Django.json'))
    scoped_credentials = credentials.with_scopes(SCOPES)
    service = build("calendar", "v3", credentials=scoped_credentials)
    return service

class HomeView(FormView):
    form_class = BookingForm
    template_name = 'calendar.html'
    car_id = 0
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        #self.car = Car.objects.get(id=HomeView.car_id)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                
                booking = Booking(
                    eventTitle=form.cleaned_data['eventTitle'],
                    startDateTime=form.cleaned_data['startDateTime'],
                    endDateTime=form.cleaned_data['endDateTime'],
                    descript=form.cleaned_data['descript'],
                    user_id = request.user.id,
                    car_id=HomeView.car_id
                )
                booking.save()

                # Handle Google Calendar Event Creation
                eventTitle = form.cleaned_data['eventTitle']
                start_date_data = form.cleaned_data['startDateTime']
                end_date_data = form.cleaned_data['endDateTime']+timedelta(days=1)
                descript = form.cleaned_data['descript']
                
            
                if start_date_data > end_date_data:
                    messages.add_message(self.request, messages.INFO, 'Please enter the correct period.')
                    return HttpResponseRedirect(reverse("home"))

                service = build_service(self.request)
                event_body = {
                    "summary": eventTitle,
                    "description": descript,
                    "start": {"dateTime": start_date_data.astimezone(pytz.timezone(TIMEZONE)).isoformat(), "timeZone": TIMEZONE},
                    "end": {"dateTime": end_date_data.astimezone(pytz.timezone(TIMEZONE)).isoformat(), "timeZone": TIMEZONE},
                }

                try:
                    event = service.events().insert(calendarId=calendarId, body=event_body).execute()
                    messages.success(self.request, 'Event created successfully!')
                    return super().form_valid(form)
                except HttpError as error:
                    messages.add_message(self.request, messages.ERROR, f" Error occurred: {error}")
                    return HttpResponseRedirect(reverse("home"))

            else:
                return self.form_invalid(form)
            

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'Form submission success!!')
        return reverse("upload_file")

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        form = BookingForm()
        booking_event = []

        service = build_service(self.request)
        try:
            events = service.events().list(calendarId=calendarId).execute()

            for event in events['items']:
                event_title = event['summary']
                start_date_time = event["start"]["dateTime"]
                end_date_time = event['end']["dateTime"]
                booking_event.append([event_title, start_date_time, end_date_time])

        except HttpError as error:
            messages.add_message(self.request, messages.ERROR, f"An error occurred: {error}")
            
        booked_dates = list(Booking.objects.values('startDateTime', 'endDateTime'))
        car_booking = list(Booking.objects.values('car_id'))
        booked_dates_json = json.dumps(booked_dates, cls=DjangoJSONEncoder)
        car_booking_json = json.dumps(car_booking, cls=DjangoJSONEncoder)
        car_id_json = json.dumps(HomeView.car_id, cls=DjangoJSONEncoder)
        
        
        context = {
            "form": form,
            "booking_event": booking_event,
            'booked_dates': booked_dates_json,
            "car_id": car_id_json,
            "car_booking": car_booking_json,
        }
        
        return context
   
def bookingDateData(request):
    bookings = Booking.objects.all()

    booked_dates = []
    for booking in bookings:
        start_date = localtime(booking.startDateTime, timezone.get_current_timezone())
        end_date = localtime(booking.endDateTime, timezone.get_current_timezone())
        car_id = booking.car
        print(car_id.car)
        booked_dates.append({
            'start': start_date.isoformat(), 
            'end': end_date.isoformat(),
        })

   
    return render(request,{'booked_dates': booked_dates})

def carList(request):
    car = Car.objects.all()
    context = {"car": car}
    return render(request, 'selectcar.html', context)

def selectedCarList(request,id):
    #car = Car.objects.get(id=id)
    HomeView.car_id = id
    return redirect("/calendar")    

@login_required
def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            booking = Booking.objects.last()
            pdf = PDFUpload.objects.last()
            pdf = PDFUpload.objects.get(id=pdf.id)
            booking.pdf = pdf
            booking.save()
            return redirect('dashboard')  # Redirect to a success page
    else:
        form = PDFUploadForm()
    booking = Booking.objects.filter(user_id=request.user.id).last()
    latest_booking = Booking.objects.filter(user=request.user).last()
    return render(request, 'upload.html', {'form': form, 'date': latest_booking, 'booking': booking})

@user_passes_test(lambda user: user.is_superuser)
def adminBooking(request):
    booking = Booking.objects.all()
    return render(request, "bookingRequest.html", {"booking": booking})

@user_passes_test(lambda user: user.is_superuser)
def updateApprove(request,id):
    booking = Booking.objects.get(id=id)
    return render(request, "requestBooking.html", {"booking": booking})

@user_passes_test(lambda user: user.is_superuser)
def updateRequest(request, id):
    booking = Booking.objects.get(id=id)
    return render(request, "requestBooking.html", {"booking": booking})
@user_passes_test(lambda user: user.is_superuser)
def updateRe(request,id):
    id_booking= request.POST["id"]
    event = request.POST["event"]
    title = request.POST["title"]
    startDateTime = request.POST["startDateTime"]
    endDateTime = request.POST["endDateTime"]
    
    is_approve = request.POST.get("is_approve") == 'on'
    
    booking = Booking.objects.get(id=id) 
    pdf = PDFUpload.objects.get(id=booking.pdf.id) 
    booking.id = id_booking
    booking.eventTitle = event
    pdf.is_approve = is_approve
    pdf.title = title
    #booking.startDateTime = startDateTime
    #booking.endDateTime = endDateTime
    #print(booking.startDateTime)
    pdf.save()
    booking.save()
    return redirect("/adminBookingRequest")
@user_passes_test(lambda user: user.is_superuser)
def deleteRequest(request,id):
    booking = Booking.objects.get(id=id)
    booking.delete()
    return redirect("/adminBookingRequest")