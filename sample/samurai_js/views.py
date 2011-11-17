from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def payment_form(request):
    return render_to_response('samurai_js/payment_form.html')

def purchase(request):
    #purchase processing done here
    pass

def receipt(request):
    return render_to_response('samurai_js/receipt.html')

