from django.contrib import admin

# Register your models here.

from .models import Chantier, Marche, Category

class ChantierAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class MarcheAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'chantier')
    list_filter = ('category', 'chantier',)
    search_fields = ('name',)


admin.site.register(Chantier, ChantierAdmin)

admin.site.register(Marche, MarcheAdmin)

admin.site.register(Category)

