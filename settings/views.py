from django.shortcuts import render
from .models import Company, Phone, SocialMediaLinks
# Create your views here.

def home(request):
    return render(request, 'settings/index.html')

def about(request):
    data = Company.objects.last()
    return render(request, 'settings/about.html', {'data':data})

def contact(request):
    data = Company.objects.last()
    phone = Phone.objects.all()
    social_media = SocialMediaLinks.objects.all()
    return render(request, 'settings/contact.html', {'data':data})    
    