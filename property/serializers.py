from rest_framework import serializers
from .models import Property



class SerializerProperty(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'