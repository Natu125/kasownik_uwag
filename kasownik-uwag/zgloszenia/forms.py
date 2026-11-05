from django import forms

from .models import Zgloszenie 


class FormularzZgloszenia(forms.ModelForm):
    class Meta:
        model = Zgloszenie
        fields = ["email", "tresc"]