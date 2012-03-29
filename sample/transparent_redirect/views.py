# Django imports
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib import messages

# Project imports
from sample.helpers import TransparentRedirectForm, parse_error

# Samurai imports
import samurai.config as config
config.merchant_key = 'a1ebafb6da5238fb8a3ac9f6'
config.merchant_password = 'ae1aa640f6b735c4730fbb56'

from samurai.payment_method import PaymentMethod as PaymentMethod
from samurai.processor import Processor as Processor

# Payment form for Transparent Redirect
# ------------------------------
#
# * Renders the transparent_redirect payment form
#
def payment_form(request):
    form = TransparentRedirectForm(auto_id='credit_card_%s')
    return render_to_response('transparent_redirect/payment_form.html', {'form': form},
                              context_instance=RequestContext(request))


# Purchase action for Transparent Redirect
# ------------------------------
#
# * Performs the purchase, and redirects the user to the purchase confirmation page
# * On error, it redirects back to the payment form to display validation/card errors
#
def purchase(request):
    token = request.GET.get('payment_method_token', None)
    trans = Processor.purchase(token, 10)
    if trans.errors:
        errors = parse_error(trans.errors)
        for err in errors:
            messages.error(request, err, fail_silently=True)
        return redirect('/transparent_redirect/payment_form')
    else:
        messages.success(request, 'Purchase Successful.', fail_silently=True)
        return render_to_response('/transparent_redirect/receipt.html')

