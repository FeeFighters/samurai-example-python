from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.utils import simplejson

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
        payment_method_token = request.POST.get('payment_method_token', None)
        ##purchase processing done here
        return_data = simplejson.dumps({'payment_method_token':payment_method_token})
        return HttpResponse(return_data)
    else:
        return HttpResponse('Pending')

# Purchase confirmation & receipt page
# ------------------------------------
def receipt(request):
    return render_to_response('samurai_js/receipt.html')

