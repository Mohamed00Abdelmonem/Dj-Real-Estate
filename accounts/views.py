from django.shortcuts import render
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def Profile(request):
    # return user.is_authontacated for return him data
    user = request.user.pk
    profile = User.objects.get(pk=user)
    return render(request, 'account/profile.html', {'profile': profile})