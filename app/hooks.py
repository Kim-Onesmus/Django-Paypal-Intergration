from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from django.conf import settings
import time

@receiver(valid_ipn_received)
def paypal_payment_received(sender, **kwargs):
    time.sleep(10)
    paypal_obj = sender
    my_invoice = str(paypal_obj.invoice)
    # match order invoice to paypal invoice
    # my_order = Order.objects.get(invoice=my_invoice)
    # my_order.paid = True
    # my_order.save()