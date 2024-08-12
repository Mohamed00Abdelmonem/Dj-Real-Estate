from django.contrib import admin
from .models import Company, Phone, SocialMediaLinks

# Inline model for Phone related to Company
class PhoneInline(admin.TabularInline):
    model = Phone
    readonly_fields = ('id',)
    extra = 1

# Inline model for SocialMediaLinks related to Company
class SocialMediaLinksInline(admin.TabularInline):
    model = SocialMediaLinks
    readonly_fields = ('id',)
    extra = 1

# Admin for Company, including inlines for Phone and SocialMediaLinks
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [PhoneInline, SocialMediaLinksInline]

# Registering Phone and SocialMediaLinks separately
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('phone', 'company')

@admin.register(SocialMediaLinks)
class SocialMediaLinksAdmin(admin.ModelAdmin):
    list_display = ('account_name', 'account_link', 'company')
