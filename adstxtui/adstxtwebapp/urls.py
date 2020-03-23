from django.urls import path
from . import views

app_name = "adstxtwebapp"
urlpatterns = [
    #path("", views.index, name="index"),
    path("", views.upload_file, name="upload_file"),
    path("uploaded/", views.file_uploaded, name="file_uploaded"),
]
