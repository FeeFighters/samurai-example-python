from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from sample.forms import TransparentRedirectForm

def payment_form(request):
    form = TransparentRedirectForm()
    return render_to_response('transparent_redirect/payment_form.html', {'form': form},
                              context_instance=RequestContext(request))
def purchase(request):
    #purchase processing done here
    pass

def receipt(request):
    return render_to_response('transparent_redirect/receipt.html')

