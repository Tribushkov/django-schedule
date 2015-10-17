from django.conf.urls import include, url, patterns
from django.contrib import admin


urlpatterns = patterns(
    url(r'^admin/', include(admin.site.urls)),
    url('', include('app.urls')),
    (r'^accounts/', include('registration.backends.simple.urls')),
)

