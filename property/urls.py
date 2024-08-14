from django.urls import path
from .views import PropertyList

app_name = 'property'

urlpatterns = [
    path('', PropertyList.as_view(), name='property_list'),
]