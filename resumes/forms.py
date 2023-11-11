from django import forms
from .models import *

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = '__all__'
