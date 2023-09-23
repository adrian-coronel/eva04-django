from django.urls import path
from . import views

urlpatterns = [
  path('login', views.signin, name='signin'),
  path('register', views.signup, name='signup'),
  path('register/store', views.store, name='store'),
  path('login/auth', views.auth, name='auth')
]