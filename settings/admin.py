from django.contrib import admin
from .models import Company, Phone, SocialMediaLinks




class PhoneTabularInline(admin.TabularInline):
    model = Phone
   
class SocialMediaLinksTabular(admin.TabularInline):
    model = SocialMediaLinks





class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'location', 'created_at')
    list_filter = ('title', 'created_at')
    search_fields = ('title', 'about', 'email', 'location')
    inlines = [PhoneTabularInline, SocialMediaLinksTabular]

admin.site.register(Company, CompanyAdmin)
