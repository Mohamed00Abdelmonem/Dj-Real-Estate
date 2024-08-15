from django.shortcuts import render
from .models import Property
from django.views.generic import ListView, DetailView



# Create your views here.


class PropertyList(ListView):
    model = Property
    template_name = 'property_list.html'
    context_object_name = 'properties'

class PropertyDetail(DetailView):
    model = Property
    template_name = 'property_detail.html'
    context_object_name = 'property'
