from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
import django.contrib.auth.views as auth_views

from user_auth.views import register, registration_done, redirect_index


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gwiz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # TODO Need to see if refactoring login processes over to user_auth module
    # url(r'^$', login_required(TemplateView.as_view(template_name='index.html')), name='home'),
    url(r'^$', login_required(redirect_index), name='home'),
    # url(r'^$', auth_views.login, name='index_login'),

    # login
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout_then_login, name='logout'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'auth_views.login'}),
    # url(r'^admin/logout/$', 'django.contrib.auth.views.logout', {'next_page': 'auth_views.login'}),

    # Registration
    url(r'^register/$', register, {'post_registration_redirect': '/registration/done/'}, name='register'),
    url(r'^registration/done/$', registration_done, name='register_done'),

    # reset user password urls
    url(r'^user/password/reset/$',
        auth_views.password_reset,
        {'post_reset_redirect' : '/user/password/reset/done/'},
        name="password_reset"),
    (r'^user/password/reset/done/$', auth_views.password_reset_done),
    (r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
     auth_views.password_reset_confirm,
     {'post_reset_redirect': '/user/password/done/'}),
    (r'^user/password/done/$', auth_views.password_reset_complete),

    #change pw
    url(r'^user/password/change/$', auth_views.password_change, name='auth_password_change'),
    url(r'^user/password/change/$',
        login_required(auth_views.password_change,
                       {'post_reset_redirect': 'home'}),
        name='auth_password_change'),
    url(r'^user/password/change/done/$',
        login_required(auth_views.password_change_done),
        name='password_change_done'),
)
