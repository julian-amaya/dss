from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sensors.views.home', name='home'),
    # url(r'^dss/', include('dss.foo.urls')),
	url(r'^data/$', 'sensors.views.data_sensores' ),

	url(r'^call_celery/$', 'sensors.views.call_celery' ),

    url(r'^mark_alert/(?P<id>\d+)$', 'sensors.views.mark_alert' ),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
