from django.db import models

# Create your models here.

class Monitores(models.Model):
    nombre= models.CharField(max_length=50)
    precio= models.IntegerField()
    cantidad= models.IntegerField()
    tamaño= models.IntegerField()
    imagen= models.CharField(max_length=400)
    

class Amplificadores(models.Model):
    nombre= models.CharField(max_length=50)
    precio= models.IntegerField()
    cantidad= models.IntegerField()
    potencia= models.IntegerField()
    imagen= models.CharField(max_length=400)
    
    
class Notebooks(models.Model):
    nombre= models.CharField(max_length=50)
    precio= models.IntegerField()
    cantidad= models.IntegerField()
    imagen= models.CharField(max_length=400)


class Usuarios(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    edad= models.IntegerField()
    email= models.CharField(max_length=50)
    password=models.CharField(max_length=16)
