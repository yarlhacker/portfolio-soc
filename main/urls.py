from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', lambda request: redirect('home#about'), name='about'),
    path('experiences/', lambda request: redirect('home#experience'), name='experiences'),
    path('contact/', lambda request: redirect('home#contact'), name='contact'),
]