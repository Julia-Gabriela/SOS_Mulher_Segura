from django import forms
from .models import Vitima

class VitimaForm(forms.ModelForm):
    class Meta:
        model = Vitima
        fields = '__all__'
