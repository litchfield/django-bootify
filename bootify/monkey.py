"""
This monkey patch will default all standard widgets to become bootstrap 3 friendly

Add this to your settings.py --

    from bootify import monkey

"""
from forms import BootForm
from forms import BootModelForm

from django import forms
forms.Form = BootForm
forms.ModelForm = BootModelForm
