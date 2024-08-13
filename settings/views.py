from django.shortcuts import render
from .models import Company, Phone, SocialMediaLinks
# Create your views here.

def home(request):
    
    return render(request, 'settings/index.html')