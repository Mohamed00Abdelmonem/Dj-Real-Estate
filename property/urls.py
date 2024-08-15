from django.urls import path
from .views import PropertyList, PropertyDetail

app_name = 'property'

urlpatterns = [
    path('', PropertyList.as_view(), name='property_list'),
    path('<int:pk>/', PropertyDetail.as_view(), name='property_detial'),  # Fixed typo in 'property_detail'
]