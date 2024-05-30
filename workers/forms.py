from django import forms
from django.forms.widgets import SelectDateWidget
from .models import Worker

class WorkerForm(forms.ModelForm):
    date_started = forms.DateField(widget=SelectDateWidget())
    class Meta:
        model = Worker
        fields = ['name', 'date_started', 'category', 'rate']