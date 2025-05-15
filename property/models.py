from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random
from location_field.models.plain import PlainLocationField


PROPERTY_TYPES = (
        ('House', 'House'),
        ('Apartment', 'Apartment'),
        ('Office', 'Office'),
        ('Land', 'Land'),
        ('Villa', 'Villa'),
        ('Shop', 'Shop'),
        ('Warehouse', 'Warehouse'))
                                    
class Property(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField(max_length=10)
    status = models.CharField(choices=(('Rent', 'Rent'), ('Sale', 'Sale'), ('Buy', 'Buy')), max_length=10)
    sku = models.IntegerField(unique=True, default=random.randint(1, 10000))
    type = models.CharField(choices=PROPERTY_TYPES, max_length=10)
    bathroom = models.IntegerField(null=True, blank=True)
    bedroom = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    parking = models.BooleanField(default=False)
    image = models.ImageField(upload_to='property')
    area = models.FloatField()
    year_built = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=9, default='30.0444,31.2357')
    video = models.FileField(upload_to='prop', null=True, blank=True)
    owner = models.ForeignKey(User, related_name='property_owner', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    view_count = models.PositiveIntegerField(default=0)  # Added field

    def get_lat_lng(self):
        """Extract latitude and longitude from the location field."""
        if self.location:
            lat_lng = self.location.split(',')
            if len(lat_lng) == 2:
                return lat_lng[0], lat_lng[1]
        return '0', '0'  # default values

    def __str__(self) -> str:
        return self.title

class ImagesProperty(models.Model):
    Image = models.ImageField(upload_to='property_images')
    property = models.ForeignKey(Property, related_name="ImagesProperty", on_delete=models.SET_NULL, null=True, blank=True)


class FloorPlansImages(models.Model):
    Image = models.ImageField(upload_to='property_images')
    property = models.ForeignKey(Property,related_name="ImageFloorProperty", on_delete=models.SET_NULL ,null=True, blank=True)    


class Features(models.Model):
    features = models.CharField(max_length=100)
    property = models.ForeignKey(Property,related_name="Features_Property", on_delete=models.SET_NULL, null=True, blank=True)

