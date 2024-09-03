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

class createProperty(CreateView):
    model = Property
    fields = '__all__'   
    template_name = 'create_property.html'
    success_url = reverse_lazy('property:property_list')  # Redirect to property list page after successful creation



class PropertyDetail(DetailView):
    model = Property
    template_name = 'property_detail.html'
    context_object_name = 'property'

    
    def get_object(self):
        obj = super().get_object()
        obj.view_count += 1
        obj.save()
        return obj