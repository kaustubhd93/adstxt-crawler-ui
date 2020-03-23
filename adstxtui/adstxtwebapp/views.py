from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import UploadFileForm
from .common import handle_uploaded_file

# Create your views here.
def index(request):
    return render(request, "adstxtwebapp/index.html", {})
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
