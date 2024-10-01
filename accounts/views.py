from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings   

from property.models import Property
from .forms import  SignupForm, ActivationForm
from .models import Profile









from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import SignupForm
from .models import Profile




# from django.http import JsonResponse

# def create_product(request):
#     name = request.POST['name']
    







def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            user = form.save(commit=False)
            user.is_active = False
            user.save()  # The signal will create the Profile here

            profile = user.profile  # This will retrieve the Profile associated with the user

            # Send an activation email
            send_mail(
                "Activate Your Account",
                f"Welcome {username} \n use this code {profile.code} to activate your account.",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return redirect(f'/accounts/{username}/activate')

    else:
        form = SignupForm()
    return render(request, 'registration/register.html', {'form': form})









from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Profile  # Ensure Profile is imported
from .forms import ActivationForm




def activate(request, username):
    # Retrieve the user and their profile
    user = get_object_or_404(User, username=username)  # Safely get the User
    profile = user.profile  # Retrieve the Profile associated with the User
    
    if request.method == 'POST':
        form = ActivationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if code == profile.code:
                # Reset the activation code
                profile.code = ''
                profile.save()  # Save the profile after modifying the code

                # Activate the user
                user.is_active = True
                user.save()  # Save the user after activating

                return redirect('/accounts/login')  # Redirect after successful activation
    else:
        form = ActivationForm()  # Create a new form instance for GET requests

    return render(request, 'registration/activate.html', {'form': form})









@login_required
def Profile(request):
    # return user.is_authontacated for return him data
    user = request.user.pk
    profile = User.objects.get(pk=user)
    propertys = Property.objects.filter(owner=user)
    return render(request, 'account/profile.html', 
                  {'profile': profile,
                   'propertys': propertys, 
                   'request': request}) # i'm returned request here for use sent my current link in whatapp 