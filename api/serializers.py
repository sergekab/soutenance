from rest_framework import serializers
from .models import Programme, Utilisateur, Evenement

class ProgrammeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programme
        fields = ['id', 'description', 'detail']

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['id', 'nom', 'email']

class EvenementSerializer(serializers.ModelSerializer):
    organisateur = UtilisateurSerializer()  # Utilise le sérialiseur Utilisateur pour le champ organisateur

    class Meta:
        model = Evenement
        fields = ['id', 'nom', 'date', 'heure', 'lieu', 'description', 'organisateur']
