from django.contrib import admin
from .models import Property, ImagesProperty, FloorPlansImages,Features 
# Register your models here.




class ImagesPropertyTabularInline(admin.TabularInline):
    model = ImagesProperty

class FloorPlansImagesTabularInline(admin.TabularInline):
    model = FloorPlansImages

class PropertyInline(admin.ModelAdmin):
    list_display = ('title', 'location', 'created_at')
    list_filter = ('city', 'created_at')
    search_fields = ('title', 'description', 'city', 'location')
    inlines = [ImagesPropertyTabularInline, FloorPlansImagesTabularInline]


admin.site.register(Property, PropertyInline)



