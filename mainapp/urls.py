from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('contact/', views.contact, name='contact'),
    path('privacy/', views.privacy, name='privacy'),
    path('about/', views.about, name='about'),
    path('dodaj_wydatek/', views.dodaj_wydatek, name='dodaj_wydatek'),
    path('zestawienia/', views.zestawienia, name='zestawienia'),
    path('dodaj_kategorie/', views.dodaj_kategorie, name='dodaj_kategorie'),
    path('kategorie/', views.lista_kategorii, name='lista_kategorii'),
]