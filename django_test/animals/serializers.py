from rest_framework import serializers
from .models import AnimalModel
from django.contrib.auth import get_user_model

User = get_user_model()


class AnimalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalModel
        fields = '__all__'


class AnimalCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalModel
        fields = ('name', 'id')


class UserDetailSerializer(serializers.ModelSerializer):
    animals = AnimalCustomSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'animals']
