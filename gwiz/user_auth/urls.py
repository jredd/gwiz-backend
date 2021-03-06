from django.contrib.auth.decorators import login_required
import django.contrib.auth.views as auth_views
from django.conf.urls import patterns, url


from . import views

urlpatterns = patterns(
    '',
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout_then_login, name='logout'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'auth_views.login'}),
    url(r'^register/$', views.register, {'post_registration_redirect': '/registration/done/'}, name='register'),
    url(r'^registration/done/$', views.registration_done, name='registration_done'),

    url(r'^user/password/reset/$', auth_views.password_reset, {'post_reset_redirect': '/user/password/reset/done/'}, name="password_reset"),
    url(r'^user/password/reset/done/$', auth_views.password_reset_done),
    url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm, {'post_reset_redirect': '/user/password/done/'}),
    url(r'^user/password/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

    # url(r'^user/password/change/$', auth_views.password_change, name='auth_password_change'),
    url(r'^user/password/change/$', login_required(auth_views.password_change, {'post_reset_redirect': 'home'}), name='auth_password_change'),
    url(r'^user/password/change/done/$', login_required(auth_views.password_change_done), name='password_change_done'),

    # REST Token Auth
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api-token-refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),

    url(r'user-detail/(?P<pk>.+)/$', views.UserDetail.as_view(), name='user_detail'),
    url(r'users-list/$', views.UsersList.as_view(), name='user_list'),

)