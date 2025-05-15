from django.shortcuts import render
from .models import Property
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

# Create your views here.


class PropertyList(ListView):
    model = Property
    template_name = 'property_list.html'
    context_object_name = 'properties'

# class createProperty(CreateView):
#     model = Property
#     fields = '__all__'   
#     template_name = 'create_property.html'
#     success_url = "/"  # Redirect to property list page after successful creation






from django.shortcuts import render, redirect
from .forms import PropertyForm, ImagePropertyForm, FloorPlanForm, FeatureForm
from .models import Property, ImagesProperty, FloorPlansImages, Features
from django.forms import modelformset_factory

def CreatePropertyView(request):
    ImageFormSet = modelformset_factory(ImagesProperty, form=ImagePropertyForm, extra=4, can_delete=True)
    FloorPlanFormSet = modelformset_factory(FloorPlansImages, form=FloorPlanForm, extra=2, can_delete=True)
    FeatureFormSet = modelformset_factory(Features, form=FeatureForm, extra=3, can_delete=True)

    if request.method == 'POST':
        property_form = PropertyForm(request.POST, request.FILES)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=ImagesProperty.objects.none(), prefix='images')
        floorplan_formset = FloorPlanFormSet(request.POST, request.FILES, queryset=FloorPlansImages.objects.none(), prefix='floorplans')
        feature_formset = FeatureFormSet(request.POST, queryset=Features.objects.none(), prefix='features')

        if property_form.is_valid() and image_formset.is_valid() and floorplan_formset.is_valid() and feature_formset.is_valid():
            # Save main property
            property_instance = property_form.save(commit=False)
            property_instance.owner = request.user  # Set logged in user
            property_instance.save()

            # Save images
            for form in image_formset.cleaned_data:
                if form and not form.get('DELETE'):
                    image = form.get('Image')
                    if image:
                        ImagesProperty.objects.create(
                            property=property_instance,
                            Image=image
                        )

            # Save floor plans
            for form in floorplan_formset.cleaned_data:
                if form and not form.get('DELETE'):
                    image = form.get('Image')
                    if image:
                        FloorPlansImages.objects.create(
                            property=property_instance,
                            Image=image
                        )

            # Save features
            for form in feature_formset.cleaned_data:
                if form and not form.get('DELETE'):
                    feature = form.get('features')
                    if feature:
                        Features.objects.create(
                            property=property_instance,
                            features=feature
                        )

            return redirect('/')  # Replace with your success URL

    else:
        property_form = PropertyForm()
        image_formset = ImageFormSet(queryset=ImagesProperty.objects.none(), prefix='images')
        floorplan_formset = FloorPlanFormSet(queryset=FloorPlansImages.objects.none(), prefix='floorplans')
        feature_formset = FeatureFormSet(queryset=Features.objects.none(), prefix='features')

    context = {
        'property_form': property_form,
        'image_formset': image_formset,
        'floorplan_formset': floorplan_formset,
        'feature_formset': feature_formset,
    }

    return render(request, 'create_property.html', context)







from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Property
from .forms import PropertyForm, ImagePropertyForm, FloorPlanForm, FeatureForm
from django.shortcuts import render

# class CreatePropertyView(CreateView):
#     model = Property
#     form_class = PropertyForm
#     template_name = 'create_property.html'
#     success_url = reverse_lazy('property_list')  # Change 'property_list' to your actual URL name
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['image_form'] = ImagePropertyForm()
#         context['floor_plan_form'] = FloorPlanForm()
#         context['feature_form'] = FeatureForm()
#         return context
    
#     def form_valid(self, form):
#         # Set the owner to the current user
#         form.instance.owner = self.request.user
#         return super().form_valid(form)
    
    


class PropertyDetail(DetailView):
    model = Property
    template_name = 'property_detail.html'
    context_object_name = 'property'

    
    def get_object(self):
        obj = super().get_object()
        obj.view_count += 1
        obj.save()
        return obj