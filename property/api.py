from rest_framework import generics
from .serializers import SerializerProperty
from .models import Property

class PropertyApi(generics.ListAPIView):
    serializer_class =  SerializerProperty
    queryset = Property.objects.all()





