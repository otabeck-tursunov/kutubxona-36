from django.db import models

from .managers import *



class Talaba(models.Model):
    ism = models.CharField(max_length=100)
    guruh = models.CharField(max_length=20)
    kurs = models.IntegerField()
    kitob_soni = models.IntegerField(default=0)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"


class Muallif(models.Model):
    ism = models.CharField(max_length=100)
    jins = models.CharField(max_length=10, choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')])
    tugilgan_sana = models.DateField()
    kitob_soni = models.IntegerField()
    tirik = models.BooleanField(default=True)

    objects = models.Manager()
    tiriklar = TirikManager()

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = "Muallif"
        verbose_name_plural = "Mualliflar"


class Kitob(models.Model):
    nom = models.CharField(max_length=200)
    janr = models.CharField(max_length=100)
    sahifa = models.IntegerField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"


class Admin(models.Model):
    ISH_VAQTI = [
        ("08:00-12:00", "08:00-12:00"),
        ("12:00-18:00", "12:00-18:00"),
    ]
    ism = models.CharField(max_length=100)
    ish_vaqti = models.CharField(max_length=50, choices=ISH_VAQTI, null=True)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Adminlar"


class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.SET_NULL, null=True)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True)
    olingan_sana = models.DateTimeField(auto_now_add=True)
    qaytarish_sana = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.talaba.ism} - {self.kitob.nom}"

    class Meta:
        verbose_name = "Qayd"
        verbose_name_plural = "Qaydlar"


