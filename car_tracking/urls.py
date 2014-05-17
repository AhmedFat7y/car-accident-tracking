from django.conf.urls import patterns, include, url
from mainapp import views
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'car_tracking.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^$', views.index),
    (r'^openid/', include('django_openid_auth.urls')),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    (r'^private/$', views.require_authentication),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)