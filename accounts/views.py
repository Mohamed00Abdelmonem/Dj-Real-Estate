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














from django.http import JsonResponse
from django.shortcuts import render
from langchain_community.llms import Ollama
from django.apps import apps
from django.db.models import Count
from django.contrib.auth.models import User

def generate_ollama3_text(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')  # Input question from user
        
        # Get all models dynamically
        models = apps.get_models()
        available_tables = {model._meta.model_name: model for model in models}
        extracted_data = {}

        # Extract data based on question
        for table_name, model in available_tables.items():
            if table_name in input_text.lower():
                # Dynamically count records for each model
                try:
                    count = model.objects.count()
                    extracted_data[table_name] = f"Total {table_name} records: {count}"
                    
                    # Optionally add titles or other fields if available
                    if hasattr(model, 'title'):  # If model has 'title' field
                        titles = ', '.join([getattr(obj, 'title') for obj in model.objects.all()])
                        extracted_data[f'{table_name}_titles'] = f"{table_name.capitalize()} Titles: {titles}"
                except Exception as e:
                    extracted_data[table_name] = f"Error fetching data from {table_name}: {str(e)}"

        # Check for specific queries on the User model
        if 'user' in input_text.lower():
            total_users = User.objects.count()  # Count users
            extracted_data['users'] = f"Total users: {total_users}"
        
        # Create dynamic query text
        extracted_data_str = '\n'.join([f"- {key}: {value}" for key, value in extracted_data.items()])
        
        prompt = f"""
        The user has asked: "{input_text}"
        Here is the data available:

        {extracted_data_str if extracted_data else "No specific data found in the database."}

        Please answer the user's question as accurately as possible, even if it is not a direct match to the data.
        """
        
        # Use the Ollama model to analyze the question
        llm = Ollama(model="llama3.2")
        try:
            generated_text = llm.invoke(prompt)  # Generate the response
            return JsonResponse({'generated_text': generated_text})  # Return as JSON
        except Exception as e:
            return JsonResponse({'error': f"An error occurred while generating a response: {str(e)}"}, status=500)

    return render(request, 'account/chatbot.html')