from django.shortcuts import render_to_response, get_object_or_404

def payment_form(request):
    return render_to_response('samurai_js/payment_form.html')
