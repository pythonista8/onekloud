from django.conf.urls import patterns, url

urlpatterns = patterns(
    'apps.home.views',
    url(r'^$', 'index', name='index'),
)
