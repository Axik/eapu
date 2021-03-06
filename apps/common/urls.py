from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    'common.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/', include('profiles.urls', 'profiles')),
    url(r'^ckeditor', include('ckeditor.urls')),
)


urlpatterns += patterns(
    'django.views.static',
    url(r'^static/(.*)$', 'serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(.*)$', 'serve', {'document_root': settings.MEDIA_ROOT}))


urlpatterns += patterns(
    'cathedra.views',
    url(r'^$', 'home_view', name='home'),
    url(r'^lectors/$', 'lectors_list', name='lectors_list'),
    url(r'^lectors/(?P<pk>\d+)/$', 'lector_detail'),
    url(r'^aspirants/(?P<pk>\d+)/$', 'aspirant_detail'),
    url(r'^technicians/(?P<pk>\d+)/$', 'technician_detail'))
