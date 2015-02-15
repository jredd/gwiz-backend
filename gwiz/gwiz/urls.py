from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
import django.contrib.auth.views as auth_views

from user_auth.views import redirect_index

urlpatterns = patterns(
    '',
    url(r'^$', login_required(redirect_index), name='home'),
    url(r'^admin/', include(admin.site.urls), name='admin_home'),
    url(r'^accounts/', include('user_auth.urls', namespace='user_auth')),

)
