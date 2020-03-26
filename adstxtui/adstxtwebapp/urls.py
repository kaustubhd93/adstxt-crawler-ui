from django.urls import path
from . import views

app_name = "adstxtwebapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.app_login, name="app_login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("upload/", views.upload_file, name="upload_file"),
    path("uploaded/", views.file_uploaded, name="file_uploaded"),
]
