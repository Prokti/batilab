from django.contrib import admin
from django.utils.text import Truncator

# Register your models here.

from .models import Chantier, Marche, Category, CalculeMaison

class ChantierAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class MarcheAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'chantier')
    list_filter = ('category', 'chantier',)
    search_fields = ('name',)

class CalculeMaisonAdmin(admin.ModelAdmin):
    list_display = ('name', 'longueur_ext', 'largueur_ext')

    fieldsets = (
        ('Général', {
            'classes': ['collapse',],
            'fields': ('name', 'longueur_ext', 'largueur_ext')
        }),
        ('CALCULES', {
            
            'fields': ('name',)
        }),

    )

    

    

admin.site.register(Chantier, ChantierAdmin)

admin.site.register(Marche, MarcheAdmin)

admin.site.register(Category)

admin.site.register(CalculeMaison, CalculeMaisonAdmin)

