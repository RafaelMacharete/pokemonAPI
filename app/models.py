from django.db import models

# Create your models here.

# Essa classe vai se portar como uma tabela do banco de dados
class Pokemon(models.Model):
    name = models.CharField(max_length=100) # Campo de texto com limitação
    url = models.TextField() # Campo de texto sem limitação

    def _str_(self):
        return self.name
    
    
class Ginasy(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    def _str_(self):
        return self.name

class GameGeneration(models.Model):
    name = models.CharField(max_length=100)
    
    ginasy = models.ForeignKey(Ginasy, verbose_name="Pokemon's Ginasy", on_delete=models.CASCADE)
    # Agora o jogo, depende de um registro de um personagem para ser criado
    ability = models.CharField(max_length=25)
    name = models.CharField(max_length=30)
    main_region = models.CharField(max_length=20)
    moves = models.CharField(max_length=25)
    pokemon_species = models.CharField(max_length=25)
    types = models.CharField(max_length=25)
    version_groups = models.CharField(max_length=50)
    created = models.DateField(editable=False, auto_now=True)
    
    def _str_(self):
        return self.name
    
# class GamePokedex(models.Model):
#     name = models.CharField(max_length=25)
#     pokedex = models.ForeignKey(GameGeneration, verbose_name='Pokedex Game', on_delete=models.CASCADE)

#     is_main_series = models.BooleanField()
#     descriptions = models.TextField()
#     name_in_another_language = models.CharField(max_length=25)
#     region = models.CharField(max_length=25)
#     version_groups = models.CharField(25)
    
#     created = models.DateField(editable=False, auto_now=True)
    
#     def _str_(self):
#         return self.name

# class PokemonRegister(models.Model):
#     name = models.CharField(max_length=30)
#     is_main_series = models.BooleanField()

#     pokedex = models.ForeignKey(GameGeneration, verbose_name='Pokedex Game', on_delete=models.CASCADE)

#     generation = models.CharField(max_length=30)
#     name_in_another_language = models.CharField(max_length=30)
#     pokemon_type = models.CharField(max_length=30)
    
#     created = models.DateField(editable=False, auto_now=True)
    
#     def _str_(self):
#         return self.name
    