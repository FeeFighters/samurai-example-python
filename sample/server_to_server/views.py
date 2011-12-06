# Django imports
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib import messages

# Project imports
from sample.helpers import ServerToServerForm, parse_error

# Samurai imports
import samurai.config as config
from samurai.payment_method import PaymentMethod as PaymentMethod
from samurai.processor import Processor as Processor
config.merchant_key = 'a1ebafb6da5238fb8a3ac9f6'
config.merchant_password = 'ae1aa640f6b735c4730fbb56'


# Payment form for Server-to-Server API
# -------------------------------------
#
# * Displays a payment form that POSTs to the purchase method below
# * The credit card data is provided directly to this django server, 
# * where it is used to process a transaction entirely on the backend.
# * A payment_method_token or reference_id can be provided in the params 
# * so that validation errors can be displayed.
#
def payment_form(request):
    form = ServerToServerForm()
    return render_to_response('server_to_server/payment_form.html', {'form': form},
                              context_instance=RequestContext(request))


# Purchase action for Server-to-Server API
# ----------------------------------------
#
# * Payment Method details are POST'ed directly to the server, which performs a S2S API call
# * NOTE: This approach is typically not recommended, as it comes with a much greater PCI compliance burden
#   In general, it is a good idea to prevent the credit card details from ever touching your server.
#
def purchase(request):
    if request.method == "POST":
        data = request.POST
        token = PaymentMethod.create(data.get('card_number'), data.get('cvv'), data.get('expiry_month'),
                                     data.get('expiry_year'), first_name=data.get('first_name'),
                                     last_name=data.get('last_name'), sandbox=True)
        trans = Processor.purchase(token.payment_method_token, 10)
        if trans.errors:
            errors = parse_error(trans.errors)
            for err in errors:
                messages.error(request, err, fail_silently=True)
            return redirect('/server_to_server/payment_form')
        else:
            messages.success(request, 'Purchase Successful.', fail_silently=True)
            return render_to_response('/server_to_server/receipt.html')
    else:
        return redirect('/server_to_server/payment_form')

