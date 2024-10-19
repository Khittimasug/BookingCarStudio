from django.shortcuts import render, redirect ,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from Test.models import users
from Test.models import UploadedFile
from Test.models import usersForm
from django.urls import reverse
from .forms import FileUploadForm

from django.shortcuts import render
from .forms import ExampleForm , TopForm

# Create your views here.
def home(request):
    return render(request ,"home.html")


def login(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        print(name, email, password)
        return redirect("data")
    else:
        return render(request ,"login.html")
    
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