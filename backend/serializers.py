from rest_framework import serializers
from .models import Historico


class HistoricoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Historico
        fields = ('id','servidor','usuario', 'script', 'terminal', 'data', 'error')