from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('paypal', include('paypal.standard.ipn.urls')),
]