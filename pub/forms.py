from django import forms
from django.db.models import fields
from .models import VideoMessageNews
class videoChek(forms.ModelForm):
    class Meta:
        model = VideoMessageNews
        fields = ['video']