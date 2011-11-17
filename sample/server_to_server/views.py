from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from sample.forms import ServerToServerForm


# Payment form for Server-to-Server API
# -------------------------------------
#
# * Displays a payment form that POSTs to the purchase method below
# * The credit card data is provided directly to this rails server, where it is used to process a
#   transaction entirely on the backend.
# * A payment_method_token or reference_id can be provided in the params so that validation errors can be displayed.
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
    #purchase processing done here
    pass


# Purchase confirmation & receipt page
# ------------------------------------
def receipt(request):
    return render_to_response('server_to_server/receipt.html')

