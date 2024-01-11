from django.db import models

class GrupoMuscular (models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Exercicio (models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    grupo_muscular = models.ForeignKey(GrupoMuscular, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome