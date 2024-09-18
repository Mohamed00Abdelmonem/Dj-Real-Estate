from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/', views.Profile, name='profile_user'),

]