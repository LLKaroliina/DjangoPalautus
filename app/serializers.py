from rest_framework import serializers
from .models import Lihasryhmat, Treeniliikkeet, Viikonpaivat, Kestavyysliikunta

class LihasryhmatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lihasryhmat
        fields = ['id' 'lihasryhmanimi']

class TreeniliikkeetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treeniliikkeet
        fields = ['id', 'liikenimi', 'paino', 'toistomaara', 'lihasryhma']  
class ViikonpaivatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viikonpaivat
        fields = ['id', 'viikonpaivanimi']
class KestavyysliikuntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kestavyysliikunta
        fields = ['id', 'liikuntalaji', 'kesto', 'viikonpaiva']