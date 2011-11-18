from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from sample.forms import TransparentRedirectForm


# Payment form for Transparent Redirect
# ------------------------------
#
# * Displays a payment form using the Samurai Rails helpers bundled in the gem
# * Payment form is initialized with PaymentMethod data, if a token is passed in the params.
#   This allows validation & processor-response error messages to be displayed.
def payment_form(request):
    form = TransparentRedirectForm(auto_id='credit_card_%s')
    return render_to_response('transparent_redirect/payment_form.html', {'form': form},
                              context_instance=RequestContext(request))

# Purchase action for Transparent Redirect
# ------------------------------
#
# * This action is requested as the callback from the Samurai.js Transparent Redirect
# * It performs the purchase, and redirects the user to the purchase confirmation page
# * On error, it redirects back to the payment form to display validation/card errors
#
def purchase(request):
    payment_method_token = request.GET.get('payment_method_token', None)
    #purchase processing done here
    return HttpResponse('Payment method token is %s. Implementation Pending' % payment_method_token)

# Purchase confirmation & receipt page
# ------------------------------------
def receipt(request):
    return render_to_response('transparent_redirect/receipt.html')

