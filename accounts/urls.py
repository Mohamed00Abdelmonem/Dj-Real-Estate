from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/', views.Profile, name='profile_user'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('gpt', views.generate_ollama3_text),

    path('<str:username>/activate', views.activate),

]