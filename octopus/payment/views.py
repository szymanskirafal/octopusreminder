from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.conf import settings

from paypal.startdard.forms import PayPalPaymentForm

def payment_process(request):

    host = request.get_host()

    paypal_dict = {
      'business': settings.PAYPAL_RECEIVER_EMAIL,
      'amount': 1,
      'item_name': 'subscritption octopus reminder',
      'invoice': '10001',
      'currency
    }

# Create your views here.
