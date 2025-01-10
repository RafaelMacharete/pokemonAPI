from django.db import models

# Create your models here.

# Essa classe vai se portar como uma tabela do banco de dados
class Pokemon(models.Model):
    name = models.CharField(max_length=100) # Campo de texto com limitação
    url = models.TextField() # Campo de texto sem limitação
    
class Game(models.Model):
    name = models.CharField(max_length=100)
    abilities = models.TextField(max_length=30)
    names = models.TextField(max_length=40)
    main_region = models.TextField(max_length=30)