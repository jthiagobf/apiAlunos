from django.db import models
from uuid import uuid4


# Create your models here.

class Cadastro(models.Model):
    id_aluno = models.UUIDField(primary_key=True, default=uuid4, editable=false )
    ano_nascimento = models.IntegerField()
    nome_aluno = models.CharField(max_Length=255)
    nome_pai = models.CharField(max_Length=255)


