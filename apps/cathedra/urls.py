from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns('cathedra.views',
                       url(r'^$', 'home_view', name='home'),
                       url(r'^lectors/$', 'lectors_list', name='lectors_list'),)
