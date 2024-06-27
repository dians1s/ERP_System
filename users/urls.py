from . import views
from django.urls import path

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('login/', views.login, name='login'),
]
