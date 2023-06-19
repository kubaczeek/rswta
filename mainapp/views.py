from django.shortcuts import render, redirect

from forms import KategoriaForm
from mainapp.models import Kategoria, Wydatek, Przychod


def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')

def privacy(request):
    return render(request, 'privacy.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def dodaj_wydatek(request):
    kategorie = Kategoria.objects.all()
    if request.method == 'POST':
        tytul = request.POST['tytul']
        kwota = request.POST['kwota']
        data = request.POST['data']
        kategoria = request.POST['kategoria']
        wydatek = Wydatek(tytul=tytul, kwota=kwota, data=data, kategoria_id=kategoria)
        wydatek.save()
    return render(request, 'dodaj_wydatek.html', {'kategorie': kategorie})

def dodaj_przychod(request):
    kategorie = Kategoria.objects.all()
    if request.method == 'POST':
        tytul = request.POST['tytul']
        kwota = request.POST['kwota']
        data = request.POST['data']
        kategoria = request.POST['kategoria']
        przychod = Przychod(tytul=tytul, kwota=kwota, data=data, kategoria_id=kategoria)
        przychod.save()
    return render(request, 'dodaj_przychod.html', {'kategorie': kategorie})

def zestawienia(request):
    wydatki = Wydatek.objects.all()
    przychody = Przychod.objects.all()
    return render(request, 'zestawienia.html', {'wydatki': wydatki, 'przychody': przychody})

def dodaj_kategorie(request):
    if request.method == 'POST':
        form = KategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_kategorii')  # Zastąp 'nazwa_widoku' odpowiednim widokiem, na który ma być przekierowane po dodaniu kategorii
    else:
        form = KategoriaForm()
    return render(request, 'dodaj_kategorie.html', {'form': form})

def lista_kategorii(request):
    kategorie = Kategoria.objects.all()
    return render(request, 'lista_kategorii.html', {'kategorie': kategorie})
