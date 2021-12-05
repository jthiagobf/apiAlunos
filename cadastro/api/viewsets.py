from rest_framework import viewsets
from cadastro.api import serializers
from cadastro import models


class CadastroViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CadastroSerializer
    queryset = models.Cadastro.objects.all()