from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.

class Company(models.Model):
    title = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='logo')
    about = models.TextField(max_length=300)
    email = models.EmailField()
    location = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Phone(models.Model):
    phone = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.phone


class SocialMediaLinks(models.Model):
    account_name = models.CharField(max_length=20)
    account_link = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.account_name