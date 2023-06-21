from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('contact/', views.contact, name='contact'),
    path('privacy/', views.privacy, name='privacy'),
    path('about/', views.about, name='about'),
    path('dodaj_wydatek/', views.dodaj_wydatek, name='dodaj_wydatek'),
    path('dodaj_przychod/', views.dodaj_przychod, name='dodaj_przychod'),
    path('zestawienia/', views.zestawienia, name='zestawienia'),
    path('dodaj_kategorie/', views.dodaj_kategorie, name='dodaj_kategorie'),
    path('kategorie/', views.lista_kategorii, name='lista_kategorii'),
    path('wykresy/', views.wykresy, name='wykresy'),
    path('usun_kategorie/<int:kategoria_id>/', views.usun_kategorie, name='usun_kategorie'),
    path('usun_wydatek/<int:wydatek_id>/', views.usun_wydatek, name='usun_wydatek'),
    path('usun_przychod/<int:przychod_id>/', views.usun_przychod, name='usun_przychod'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
