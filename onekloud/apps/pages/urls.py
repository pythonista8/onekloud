from django.conf.urls import patterns, url

urlpatterns = patterns(
    'apps.pages.views',
    url(r'^$', 'home', name='home'),
    url(r'^pricing/$', 'pricing', name='pricing'),
    url(r'^contact/$', 'contact', name='contact'),
)
