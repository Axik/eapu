from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns('cathedra.views',
                       url(r'^$', TemplateView.as_view(template_name='cathedra/home.html'), name='home'),
                       url(r'^lectors/$', 'lectors_list', name='lectors_list'),)
