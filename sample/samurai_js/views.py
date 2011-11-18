# Django imports
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.utils import simplejson

# Project imports
from sample.helpers import parse_error

# Samurai imports
import samurai.config as config
from samurai.payment_method import PaymentMethod as PaymentMethod
from samurai.processor import Processor as Processor
config.merchant_key = 'a1ebafb6da5238fb8a3ac9f6'
config.merchant_password = 'ae1aa640f6b735c4730fbb56'


# Payment form for Samurai.js
# ------------------------------
#
# * displays a drop-in payment form from Samurai.js, no extra logic required
def payment_form(request):
    return render_to_response('samurai_js/payment_form.html',
                              context_instance=RequestContext(request))

# Purchase action for Samurai.js
# ------------------------------
#
# * payment_method_token is POST'd via AJAX
# * Responds with a JSON transaction object
#
def purchase(request):
    if request.method == 'POST':
        token = request.POST.get('payment_method_token', None)
        trans = Processor.purchase(token, 10)
        return_data = simplejson.dumps({'payment_method_token':token},
                                        {'transaction': trans})
        return HttpResponse(return_data)
    else:
        return redirect('/samurai_js/payment_form')

