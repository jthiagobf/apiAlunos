from rest_framework import serializers
from cadastro import models


class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cadastro
        fields = '__all__'
