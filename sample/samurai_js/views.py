from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

# Payment form for Samurai.js
# ------------------------------
#
# * displays a drop-in payment form from Samurai.js, no extra logic required
def payment_form(request):
    return render_to_response('samurai_js/payment_form.html')


# Purchase action for Samurai.js
# ------------------------------
#
# * payment_method_token is POST'd via AJAX
# * Responds with a JSON transaction object
#
def purchase(request):
    #purchase processing done here
    pass


# Purchase confirmation & receipt page
# ------------------------------------
def receipt(request):
    return render_to_response('samurai_js/receipt.html')

