from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from classroom.models import ClassromEntity
from django.views import View


class ClassForm(forms.Form):
    id = forms.IntegerField(required=True)
    name = forms.CharField(max_length=255, required=True)
    date = forms.DateTimeField() 
    description = forms.CharField(max_length=255, required=True)
    discipline = forms.CharField(max_length=255, required=True)
    reservation = forms.BooleanField()

    # def __init__(self, *args, **kwargs):
    #     self.fields['temperature'].label = 'Temperatura'