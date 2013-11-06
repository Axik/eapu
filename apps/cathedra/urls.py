from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from cathedra.views import LectorsListView


urlpatterns = patterns('',
    url(r'^home/', TemplateView.as_view(template_name="cathedra/home.html")),
    url(r'^lectors/', LectorsListView.as_view(), name='list'),
)
