# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import brokenroad, Desa
from django.db.models import Count

# Register your models here.

class brokenroadAdmin(LeafletGeoAdmin):
    list_display =('nama','desa','kerusakan','deskripsi','status','lokasi','gambar')

    actions = ['make_fixed','make_unfixed']

    def make_fixed(modeladmin, request, queryset):
        queryset.update(status='s')
    make_fixed.short_description = "Mark selected Broken Roads as fixed"

    def make_unfixed(modeladmin, request, queryset):
        queryset.update(status='b')
    make_unfixed.short_description = "Mark selected Broken Roads as not fixed"

class desaAdmin(admin.ModelAdmin):
    list_display = ('desa','kecamatan','total_broken_count')

    def get_queryset(self, request):
        qs = super(desaAdmin, self).get_queryset(request)
        qs = qs.annotate(broken_count=Count('brokenroad')).filter(brokenroad__status='b')
        return qs

    def total_broken_count(self, obj):
        return obj.broken_count

    total_broken_count.admin_order_field = '-broken_count'

admin.site.register(brokenroad, brokenroadAdmin)
admin.site.register(Desa, desaAdmin)

