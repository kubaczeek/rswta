from django import forms

from mainapp.models import Kategoria


class KategoriaForm(forms.ModelForm):
    class Meta:
        model = Kategoria
        fields = ['nazwa']