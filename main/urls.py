from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.home, name='about'),
    path('experiences/', views.home, name='experiences'),
    path('contact/', views.home, name='contact'),
]