from django.urls import path
from .views import PropertyList, PropertyDetail, CreatePropertyView
from .api import PropertyApi, PropertyDetailApi
app_name = 'property'

urlpatterns = [
    path('', PropertyList.as_view(), name='property_list'),
    path('<int:pk>/', PropertyDetail.as_view(), name='property_detial'),  # Fixed typo in 'property_detail'
    path('add/', CreatePropertyView, name='create_property'),


    # API
    path('api/properties/', PropertyApi.as_view()),
    path('api/properties/<int:pk>', PropertyDetailApi.as_view()),

]