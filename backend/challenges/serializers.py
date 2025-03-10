from rest_framework import serializers
from .models import Challenge, Book

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = '__all__'
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'