from django import forms
from .models import *

class add(forms.Form):
    name = models.CharField(max_length=100, null=False, blank=False)
    


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']