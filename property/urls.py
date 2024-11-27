from django.urls import path
from .views import PropertyList, PropertyDetail, createProperty
from .api import PropertyApi
app_name = 'property'

urlpatterns = [
    path('', PropertyList.as_view(), name='property_list'),
    path('<int:pk>/', PropertyDetail.as_view(), name='property_detial'),  # Fixed typo in 'property_detail'
    path('add/', createProperty.as_view(), name='create_property'),


    # API
    path('api/properties/', PropertyApi.as_view())

]