from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view.as_view(), name='home_view'),
    path('about/', views.about_view.as_view(), name='about_view'),
    path('FAQ/', views.faq, name='FAQ-Page'),
    path('contact/', views.contact, name='Contact-Page'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]

