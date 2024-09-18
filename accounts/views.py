from django.shortcuts import render
from .models import Profile
from property.models import Property
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def Profile(request):
    # return user.is_authontacated for return him data
    user = request.user.pk
    profile = User.objects.get(pk=user)
    propertys = Property.objects.filter(owner=user)
    return render(request, 'account/profile.html', 
                  {'profile': profile,
                   'propertys': propertys, 
                   'request': request}) # i'm returned request here for use sent my current link in whatapp 