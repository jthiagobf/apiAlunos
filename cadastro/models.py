from django.db import models
from uuid import uuid4


# Create your models here.

class Cadastro(models.Model):
    id_aluno = models.UUIDField(primary_key=True, default=uuid4, editable=false)
    nome_aluno = models.CharField(max_Length=255)
    ano_nascimento = models.DateField(auto_now_add=True)
    nome_mae = models.CharField(max_length=255)
    nome_pai = models.CharField(max_Length=255)
    ano_ingresso = models.DateField(auto_now_add=True)
    turma = models.CharField(max_length=255)
    serie = models.CharField(max_length=10)


