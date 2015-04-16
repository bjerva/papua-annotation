from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^papua_dictionary/$', 'annotation.views.index'),
    (r'^papua_dictionary/search_helper/$', 'annotation.views.search_helper'),
    (r'^papua_dictionary/add_new/$', 'annotation.views.add_new'),
    (r'^papua_dictionary/search/(?P<string>.+)/$', 'annotation.views.search'),
    (r'^papua_dictionary/(?P<entry_id>\d+)/$', 'annotation.views.detail'),
    (r'^papua_dictionary/(?P<entry_id>\d+)/results/$', 'annotation.views.results'),
    (r'^papua_dictionary/(?P<entry_id>\d+)/add/$', 'annotation.views.add'),
    (r'^admin/', include(admin.site.urls)),
)
