# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.core.serializers import serialize
from django.http import HttpResponse
from django.urls import reverse_lazy
from models import Desa, brokenroad
from django import forms
from leaflet.forms.widgets import LeafletWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

class BrokenRoadForm(forms.ModelForm):
    class Meta:
        model = brokenroad
        fields = ('nama','kerusakan','deskripsi','desa','lokasi','gambar')
        widgets = {'lokasi': LeafletWidget()}
        labels = {
            "nama": "Nama Kerusakan",
            "kerusakan": "Tingkat Kerusakan",
            "deskripsi": "Deskripsi Kerusakan",
            "desa": "Wilayah Administrasi (Desa)"
        }

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

class FixedRoadsView(TemplateView):
    template_name = 'brokenFixed.html'

class NotFixedRoadsView(TemplateView):
    template_name = 'brokenNotFixed.html'

def desa_datasets(request):
    desa = serialize('geojson', Desa.objects.all())
    return HttpResponse(desa,content_type='json')

def brokenroadunfixed_datasets(request):
    brokenRoad = serialize('geojson', brokenroad.objects.filter(status='b'))
    return HttpResponse(brokenRoad,content_type='json')

def brokenroadfixed_datasets(request):
    brokenRoad = serialize('geojson', brokenroad.objects.filter(status='s'))
    return HttpResponse(brokenRoad,content_type='json')


# Views User Input Data
class DataInput(CreateView):
    model = brokenroad
    form_class = BrokenRoadForm
    success_url = reverse_lazy('home')
    template_name = 'brokenroad_form.html'
