from django.conf.urls import patterns, include, url
from font.views import  *
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

#    url(r'^register/$', TemplateView.as_view(template_name='register.html')),
    url(r'^$', view_register),
    url(r'^register/$', view_register),
    url(r'^register_btn/$', register_btn),
    url(r'^login/$', view_login),
    url(r'^login_btn/$', login_btn),

    url(r'^home/$', view_home),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

