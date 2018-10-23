# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from adminsortable.models import SortableMixin
from django.db.models import Count

# Create your models here.

class Desa(models.Model):
    desa = models.CharField(max_length=40)
    kecamatan = models.CharField(max_length=18)
    kabupaten = models.CharField(max_length=14)
    propinsi = models.CharField(max_length=9)
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        ordering = ('desa',)

    def __unicode__(self):
        return "{0} Kec. {1}".format(self.desa, self.kecamatan)

class brokenroad(models.Model):
    KERUSAKAN_CHOICES = (
        ("Rusak Ringan","Rusak Ringan"),
        ("Rusak Sedang","Rusak Sedang"),
        ("Rusak Berat","Rusak Berat"),
        ("Rusak Total","Rusak Total"),
    )

    STATUS_CHOICES = (
        ('b', 'Belum Diperbaiki'),
        ('s', 'Sudah Diperbaiki'),
    )

    nama = models.CharField(max_length=50)
    kerusakan = models.CharField(max_length=20,
                    choices=KERUSAKAN_CHOICES,
                    default="Rusak Ringan")
    deskripsi = models.TextField(max_length=500, default="Isikan Deskripsi Kerusakan...")
    desa = models.ForeignKey(Desa, on_delete=models.SET_NULL, null=True)
    lokasi = models.PointField(srid=4326)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='b')
    gambar = models.ImageField(upload_to = 'images/', default = 'images/None/no-img.jpg')
    objects = models.GeoManager()

    def __unicode__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Broken Roads"
