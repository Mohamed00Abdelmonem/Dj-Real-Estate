from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(UserCreationForm):
    # Fields from the User model
    email = forms.EmailField(required=True)
    
    # Fields from the Profile model
    phone = forms.CharField(max_length=15, required=False)
    image = forms.ImageField(required=False)
    name = forms.CharField(max_length=50, required=False)
    about = forms.CharField(widget=forms.Textarea, required=False)
    address = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone', 'image', 'name', 'about', 'address']

    def save(self, commit=True):
        # First, save the User part of the form
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        user.save()

        # Then create or update the Profile model
        Profile.objects.create(
            user=user,
            phone_number = self.cleaned_data['phone'],
            image = self.cleaned_data['image'],
            name = self.cleaned_data['name'],
            about = self.cleaned_data['about'],
       
        
            
            )

        return user
    

    

class ActivationForm(forms.Form):
    code = forms.CharField(max_length=8)
