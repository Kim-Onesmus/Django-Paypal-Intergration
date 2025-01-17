from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('paypal', include('paypal.standard.ipn.urls')),
    path('payment_success', views.PaymentSuccess, name='payment_success'),
    path('payment_failed', views.PaymentFailed, name='payment_failed'),
]