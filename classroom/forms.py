from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from .models import WeatherEntity
from django.views import View


class WeatherForm(forms.Form):
    id = forms.IntegerField(read_only=True)
    name = forms.CharField(max_length=255, allow_blank=True)
    date = forms.DateTimeField() 
    description = forms.CharField(max_length=255, allow_blank=True)
    discipline = forms.CharField(max_length=255, allow_blank=True)
    reservation = forms.BooleanField()

    # def __init__(self, *args, **kwargs):
    #     self.fields['temperature'].label = 'Temperatura'