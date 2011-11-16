from django.shortcuts import render_to_response, get_object_or_404
from sample.forms import ServerToServerForm

def payment_form(request):
    form = ServerToServerForm()
    return render_to_response('server_to_server/payment_form.html', {'form': form})
