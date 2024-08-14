from django.contrib import admin
from .models import Property, ImagesProperty, FloorPlansImages,Features 
# Register your models here.


admin.site.register(Property)
admin.site.register(ImagesProperty)
admin.site.register(FloorPlansImages)
admin.site.register(Features)