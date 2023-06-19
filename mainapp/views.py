import matplotlib
from django.db.models import Sum
from django.shortcuts import render, redirect
import seaborn as sns
import matplotlib.pyplot as plt
matplotlib.use('agg')


from forms import KategoriaForm
from mainapp import models
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

def wykresy(request):
    # Pierwszy wykres - ogólne porównanie wydatków do przychodów
    wydatki_suma = Wydatek.objects.aggregate(suma_wydatkow=Sum('kwota'))['suma_wydatkow']
    przychody_suma = Przychod.objects.aggregate(suma_przychodow=Sum('kwota'))['suma_przychodow']
    labels = ['Wydatki', 'Przychody']
    values = [wydatki_suma, przychody_suma]
    plt.figure(figsize=(6, 4))
    plt.bar(labels, values)
    plt.xlabel('Rodzaj')
    plt.ylabel('Suma')
    plt.title('Porównanie wydatków do przychodów')
    plt.savefig('media/images/wykres1.png')  # Zapisz wykres jako plik graficzny
    plt.close()  # Zamknij bieżący wykres, aby zwolnić pamięć

    # Drugi wykres - szczegółowe informacje na temat wydatków
    kategorie = Kategoria.objects.all()
    wydatki_kategorie = []
    for kategoria in kategorie:
        suma_kategorii = Wydatek.objects.filter(kategoria=kategoria).aggregate(suma_kwoty=models.Sum('kwota'))['suma_kwoty']
        if suma_kategorii:
            wydatki_kategorie.append((kategoria.nazwa, suma_kategorii))
    wydatki_kategorie.sort(key=lambda x: x[1], reverse=True)  # Sortuj według sumy kwoty malejąco
    kategorie_labels = [kategoria[0] for kategoria in wydatki_kategorie]
    kategorie_values = [kategoria[1] for kategoria in wydatki_kategorie]
    plt.figure(figsize=(8, 6))
    sns.barplot(x=kategorie_values, y=kategorie_labels)
    plt.xlabel('Suma')
    plt.ylabel('Kategoria')
    plt.title('Szczegółowe informacje na temat wydatków')
    plt.savefig('media/images/wykres2.png')
    plt.close()

    # Trzeci wykres - szczegółowe informacje na temat przychodów
    przychody_kategorie = []
    for kategoria in kategorie:
        suma_kategorii = Przychod.objects.filter(kategoria=kategoria).aggregate(suma_kwoty=models.Sum('kwota'))['suma_kwoty']
        if suma_kategorii:
            przychody_kategorie.append((kategoria.nazwa, suma_kategorii))
    przychody_kategorie.sort(key=lambda x: x[1], reverse=True)
    kategorie_labels = [kategoria[0] for kategoria in przychody_kategorie]
    kategorie_values = [kategoria[1] for kategoria in przychody_kategorie]
    plt.figure(figsize=(8, 6))
    sns.barplot(x=kategorie_values, y=kategorie_labels)
    plt.xlabel('Suma')
    plt.ylabel('Kategoria')
    plt.title('Szczegółowe informacje na temat przychodów')
    plt.savefig('media/images/wykres3.png')
    plt.close()

    return render(request, 'wykresy.html')
