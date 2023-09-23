from django.urls import path
from . import views

urlpatterns = [
  path('formapp/', views.showForm, name='formapp'),
  path('formapp/calculate/', views.calculate, name='calculate'),
]