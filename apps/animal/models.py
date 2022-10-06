from django.db import models
from apps.pessoa.models import Pessoa

# Create your models here.
class Animal(models.Model):
    nome = models.CharField(max_length=50)
    especie = models.CharField(max_length=30)
    idade = models.IntegerField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        # return self.nome
        return f'{self.especie} : {self.nome}'
