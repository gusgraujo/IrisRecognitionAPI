from django.db import models
from datetime import date


class Iris (models.Model):
    
    nome = models.CharField(max_length=200)
    usuario = models.CharField(max_length=30,default='user')
    password = models.CharField(max_length=30,default='123')
    data_registro = models.DateField(default=date.today)
    upload = models.FileField(upload_to= r"E:\TCC\image_iris")

    def __str__(self):
        return self.usuario


#class Usuario(models.Model):
    #id_usuario = id_iris = models.IntegerField(default = 0)0