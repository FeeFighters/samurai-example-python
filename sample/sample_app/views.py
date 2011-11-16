from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from sample.sample_app.models import *
from sample.sample_app.forms import OrderForm

def home(request):
    articles = Articles.objects.all().values()
    return render_to_response('sample_app/home.html', {'articles': articles})

def articles(request):
    articles = Articles.objects.all().values()
    return render_to_response('sample_app/home.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Articles, pk=article_id)
    if purchased():
        return render_to_response('sample_app/detail.html', {'article': article})
    else:
        form = OrderForm()
        return render_to_response('sample_app/order.html', {'form': form})

def order():
    pass

def purchased():
    return False
