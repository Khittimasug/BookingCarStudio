from django.shortcuts import render, redirect ,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from Test.models import users
from Test.models import UploadedFile,carBooking,car
from Test.models import usersForm
from django.urls import reverse

from .forms import FileUploadForm,addRegister

from .forms import ExampleForm , TopForm,phone

from .forms import FileUploadForm

from .forms import ExampleForm , TopForm

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from .forms import PDFUploadForm
from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from django.views.generic import FormView
import pytz

TIMEZONE = "Asia/Bangkok"

SCOPES = ["https://www.googleapis.com/auth/calendar"]
calendarId = ("c_8aad91cf2490fc5903dde7745e60a4315f4618937af23310b9ee0fbeb6820a8a@group.calendar.google.com")

# Create your views here.
def home(request):
    return render(request ,"home.html")


'''def login(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        print(name, email, password)
        return redirect("data")
    else:
        return render(request ,"login.html")'''
    
def data(request):
    all_users = usersForm.objects.all()
    return render(request ,"data.html",{"all_users": all_users})

def form(request):
    return render(request ,"informations_form.html")

def success(request):
    return render(request ,"success.html")

def form_view(request):
    if request.method == 'POST':
        form = TopForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("success"))
    else:
        form = TopForm()
    context = {'form': form}
    return render(request, 'form.html', context)


def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})

def success(request):
    return render(request, 'upload_success.html')

def uploadList(request):
    upload_file = UploadedFile.objects.all()
    context = {"upload_file": upload_file}
    return render(request, 'upload_list.html', context)

def carList(request):
    carListfile = car.objects.all()
    context = {"carListfile": carListfile}
    return render(request, 'selectcar.html', context)

def selected(request):
    return render(request, 'selected.html')

def Calendar(request):
    return render(request ,"calendar.html")

def build_service(request):
    credentials = service_account.Credentials.from_service_account_file(('Dj.json'))
    scoped_credentials = credentials.with_scopes(SCOPES)
    service = build("calendar", "v3", credentials=scoped_credentials)
    return service

class HomeView(FormView):
    form_class = BookingForm
    template_name = 'calendar.html'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                booking = Booking(
                    eventTitle=form.cleaned_data['eventTitle'],
                    startDateTime=form.cleaned_data['startDateTime'],
                    endDateTime=form.cleaned_data['endDateTime'],
                    descript=form.cleaned_data['descript']
                )
                booking.save()

                # Handle Google Calendar Event Creation
                eventTitle = form.cleaned_data['eventTitle']
                start_date_data = form.cleaned_data['startDateTime']
                end_date_data = form.cleaned_data['endDateTime']
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
                    messages.add_message(self.request, messages.ERROR, f"Fuck Error occurred: {error}")
                    return HttpResponseRedirect(reverse("home"))

            else:
                return self.form_invalid(form)

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'Form submission success!!')
        return reverse("selectcar")

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

        context = {
            "form": form,
            "booking_event": booking_event, 
        }
        
        return context
    
def register_view(request):
    if request.method == "POST":
        form2 = phone(request.POST)
        form3 = addRegister(request.POST)
        if form3.is_valid():
            print(form2)
            print("Test")
            user = form3.save()
            user2 = form2.save()
            login(request,user)
            return redirect("dashboard")
    else:
        initial_data = {'first_name':"",'last_name':"" , 'email':"",'username':"", 'password1':"", 'password2':""}
        initial_data2 = {'phone':""}
        form3 = addRegister(initial=initial_data)
        form2 = phone(initial=initial_data2)
        return render(request, 'auth/register.html',{'form3':form3,'form2':form2})

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to a success page
    else:
        form = PDFUploadForm()
    
    return render(request, 'upload.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect("dashboard")
    else:
        initial_data = {"username":'', "password1":''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html',{'form':form})

def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect("login")