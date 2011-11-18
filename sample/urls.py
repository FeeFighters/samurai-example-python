from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', direct_to_template, {'template': 'home.html'}),
    # url(r'^sample/', include('sample.foo.urls')),

    url(r'^samurai_js/payment_form/$', 'sample.samurai_js.views.payment_form', name='samurai_js_payment_form'),
    url(r'^samurai_js/purchase/$', 'sample.samurai_js.views.purchase', name='samurai_js_purchase'),
    url(r'^samurai_js/receipt/$', 'sample.samurai_js.views.receipt', name='samurai_js_receipt'),

    url(r'^server_to_server/payment_form/$', 'sample.server_to_server.views.payment_form',
        name='server_to_server_payment_form'),
    url(r'^server_to_server/purchase/$', 'sample.server_to_server.views.purchase',
        name='server_to_server_purchase'),
    url(r'^server_to_server/receipt/$', 'sample.server_to_server.views.receipt',
        name='server_to_server_receipt'),

    url(r'^transparent_redirect/payment_form/$', 'sample.transparent_redirect.views.payment_form',
        name='transparent_redirect_payment_form'),
    url(r'^transparent_redirect/purchase/$', 'sample.transparent_redirect.views.purchase',
        name='transparent_redirect_purchase'),
    url(r'^transparent_redirect/receipt/$', 'sample.transparent_redirect.views.receipt',
        name='transparent_redirect_receipt'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
