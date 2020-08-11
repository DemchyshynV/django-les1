from rest_framework import generics
from .serializers import AnimalDetailSerializer, AnimalCustomSerializer, UserDetailSerializer, User
from .models import AnimalModel


class AnimalCreateView(generics.CreateAPIView):
    serializer_class = AnimalDetailSerializer


class AnimalDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnimalDetailSerializer
    queryset = AnimalModel.objects.all()


class AnimalAllView(generics.ListAPIView):
    serializer_class = AnimalCustomSerializer
    queryset = AnimalModel.objects.all()


class UserAllView(generics.ListAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
