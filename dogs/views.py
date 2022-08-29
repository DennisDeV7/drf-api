from .models import Dog
from rest_framework import generics
from .serializers import DogSerializer

class DogList(generics.ListCreateAPIView):
  # anything that inherits from ListAPI View is going to need 2 things
  # What is the collection of things, aka the query set
  # Serializer _class
  queryset = Dog.objects.all()
  serializer_class = DogSerializer

class DogDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Dog.objects.all()
  serializer_class = DogSerializer

