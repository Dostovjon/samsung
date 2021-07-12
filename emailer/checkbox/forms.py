from django import forms
from . models import *
from django.forms import ModelForm


class ImagerForm(forms.ModelForm):

    class Meta:
        model = Imager
        fields = '__all__'