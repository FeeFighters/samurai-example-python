from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', direct_to_template, {'template': 'home.html'}),
    # url(r'^sample/', include('sample.foo.urls')),
    url(r'^articles/$', 'sample.sample_app.views.articles', name='articles'),
    url(r'^articles/(?P<article_id>\d+)/$', 'sample.sample_app.views.article_detail', name='article_detail'),
    url(r'^order/$', 'sample.sample_app.views.order', name='order'),
    url(r'^samurai_js/$', 'sample.samurai_js.views.payment_form', name='samurai_js'),
    url(r'^server_to_server/$', 'sample.server_to_server.views.payment_form', name='server_to_server'),
    url(r'^transparent_redirect/$', 'sample.transparent_redirect.views.payment_form', name='transparent_redirect'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
