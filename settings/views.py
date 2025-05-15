from django.shortcuts import render
from .models import Company, Phone, SocialMediaLinks
from property import models
from django.core.cache import cache
# Create your views here.

def home(request):
    propertys = models.Property.objects.order_by("-created_at")[:6]
    session_data = request.session.items()  # عرض جميع بيانات الجلسة
    # requ  est.session.flush()  # يحذف جميع بيانات الجلسة

    print(session_data)

    # cache.set('propertys', propertys, 60 * 15)  # Cache for 15 minutes
    return render(request, 'settings/index.html', {'propertys':propertys})

def about(request):
    data = Company.objects.last()
    return render(request, 'settings/about.html', {'data':data})

def contact(request):
    data = Company.objects.last()
    phone = Phone.objects.all()
    social_media = SocialMediaLinks.objects.all()
    return render(request, 'settings/contact.html', {'data':data})    
    