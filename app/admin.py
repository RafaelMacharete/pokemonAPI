from django.contrib import admin
from .models import *

# Register your models here.

class datPokemon(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 10
    
admin.site.register(Pokemon, datPokemon)