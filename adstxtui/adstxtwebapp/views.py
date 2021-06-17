from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from .forms import UploadFileForm
from .common import handle_uploaded_file

# Create your views here.
def app_login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("adstxtwebapp:dashboard", args=(),))
    else:
        return render(request, "adstxtwebapp/index.html", {"error_message": "Bad credentials."})

def index(request):
    return render(request, "adstxtwebapp/index.html", {})

def dashboard(request):
    return render(request, "adstxtwebapp/dashboard.html", {})
    #return HttpResponse("Form coming soon to upload file with list of domains.")

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid")
            handle_uploaded_file(request.FILES["file"])
            return HttpResponseRedirect(reverse("adstxtwebapp:file_uploaded", args=(),))
        else:
            print("Form not valid")
    else:
        form = UploadFileForm()
    return render(request, "adstxtwebapp/upload.html", {"form": form})

def file_uploaded(request):
    return render(request, "adstxtwebapp/uploaded.html", {})
