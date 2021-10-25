from django.db import models
from datetime import date


class Iris (models.Model):
    
    nome = models.CharField(max_length=200)
    usuario = models.CharField(max_length=30,default='user')
    password = models.CharField(max_length=30,default='123')
    chave_privada = models.CharField(max_length=100,default='chave')
    chave_publica = models.CharField(max_length=1000,default='chave')
    data_registro = models.DateField(default=date.today)
    upload = models.CharField(max_length=100,default='Amostra1.jpg')

    iris_codep1 = models.CharField(max_length=1000,default='0101010')
    iris_codep2 = models.CharField(max_length=1000,default='0101010')

    def __str__(self):
        return self.usuario

