from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^home/', TemplateView.as_view(template_name="cathedra/home.html")),
)
