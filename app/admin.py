from django.contrib import admin
from .models import *

# Register your models here.

# Pokemon Info
class datPokemon(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 10
    
admin.site.register(Pokemon, datPokemon)

# Ginasy Info
class datGinasy(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 10
    
admin.site.register(Ginasy, datGinasy)

# GameGeneration Info
class datGameGeneration(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 10
    
admin.site.register(GameGeneration, datGameGeneration)

# Game Pokedex Info

# class datGamePokedex(models.Model):
#     list_display = ('id', 'name')
#     list_display_links = ('id',)
#     search_fields = ('name',)
#     list_per_page = 10

# admin.site.register(GamePokedex, datGamePokedex)

# # Pokemon Entry Info

# class datPokemonEntry(models.Model):
#     list_display = ('id', 'name')
#     list_display_links = ('id',)
#     search_fields = ('name',)
#     list_per_page = 10


# # Pokemon Register Info

# class datPokemonRegister(models.Model):
#     list_display = ('id', 'name')
#     list_display_links = ('id',)
#     search_fields = ('name',)
#     list_per_page = 10

# admin.site.register(PokemonRegister, datPokemonRegister)
