from django.shortcuts import render
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid

# Create your views here.

def Index(request):
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': 10,
        'item_name': 'Oreder',
        'no_shipping': '2',
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url;': 'https://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url;': 'https://{}{}'.format(host, reverse('payment_success')),
        'cancel_return;': 'https://{}{}'.format(host, reverse('payment_failed')),
    }
    paypal_form = PayPalPaymentsForm(initial=paypal_dict)

    return render(request, 'index.html', {'paypal_form':paypal_form})

def PaymentSuccess(request):
    return render(request, 'payment_success.html')

def PaymentFailed(request):
    return render(request, 'payment_failed.html')