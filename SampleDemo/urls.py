from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

from SampleDemo.views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SampleDemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),

    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})$', hours_ahead),
)
