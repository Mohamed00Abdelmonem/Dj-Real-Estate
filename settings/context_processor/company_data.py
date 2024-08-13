from settings.models import Company, SocialMediaLinks, Phone



def company_data(request):
    data = Company.objects.last()
    social_media = SocialMediaLinks.objects.all()
    phone = Phone.objects.all()
    return {'company_data': data, 'social_media': social_media, 'phone': phone}
