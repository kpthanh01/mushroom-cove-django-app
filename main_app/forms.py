from django import forms
from .models import Tracking

class TrackingFrom(forms.ModelForm):
  class Meta:
    model = Tracking
    fields = ['name', 'scientific', 'description']
    widgets = {
      'date': forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={
          'placeholder': 'Select a date',
          'type': 'date'
        }
      )
    }