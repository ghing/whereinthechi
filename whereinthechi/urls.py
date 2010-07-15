from django.conf.urls.defaults import *
from django.contrib.gis import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^api/(?P<output>json)/$', 'core.views.api')
)