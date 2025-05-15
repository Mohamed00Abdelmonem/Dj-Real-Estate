from django import forms
from .models import Property, ImagesProperty, FloorPlansImages, Features

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'year_built': forms.DateInput(attrs={'type': 'date'}),
        }
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].widget.attrs.update({'id': 'id_location', 'class': 'form-control'})
    
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # You can add customizations here if needed
    #     self.fields['owner'].queryset = User.objects.all()  # Example customization

class ImagePropertyForm(forms.ModelForm):
    class Meta:
        model = ImagesProperty
        fields = ['Image']

class FloorPlanForm(forms.ModelForm):
    class Meta:
        model = FloorPlansImages
        fields = ['Image']

class FeatureForm(forms.ModelForm):
    class Meta:
        model = Features
        fields = ['features']