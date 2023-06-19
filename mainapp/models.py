from django.db import models
from django.db.models import Sum

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Student(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=100)
    objects = models.Manager()  # Dodana deklaracja atrybutu 'objects'

    def __str__(self):
        return self.nazwa

class Wydatek(models.Model):
    tytul = models.CharField(max_length=100)
    kwota = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    objects = models.Manager()  # Dodana deklaracja atrybutu 'objects'

    def __str__(self):
        return self.tytul

class Przychod(models.Model):
    tytul = models.CharField(max_length=100)
    kwota = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    objects = models.Manager()  # Dodana deklaracja atrybutu 'objects'

    def __str__(self):
        return self.tytul
