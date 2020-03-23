from django import forms

class UploadFileForm(forms.Form):
    print("Class UploadFileForm called.")
    title = forms.CharField(max_length=50)
    file = forms.FileField()
