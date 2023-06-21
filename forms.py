from django import forms

from mainapp.models import Kategoria, Wydatek, Przychod


class KategoriaForm(forms.ModelForm):
    class Meta:
        model = Kategoria
        fields = ['nazwa']

class WydatekForm(forms.ModelForm):
    class Meta:
        model = Wydatek
        fields = ['tytul', 'kwota', 'data', 'kategoria']

class PrzychodForm(forms.ModelForm):
    class Meta:
        model = Przychod
        fields = ['tytul', 'kwota', 'data', 'kategoria']