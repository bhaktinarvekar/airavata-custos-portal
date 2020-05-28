from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'custos_portal_auth'
urlpatterns = [
    path('login/', views.start_login, name='login'),
    url(r'^login-password$', views.start_username_password_login, name='login_with_password'),
    url(r'^redirect_login/(\w+)/$', views.redirect_login, name='redirect_login'),
    url(r'^create-account$', views.create_account, name='create_account'),
    url(r'^redirect_login/(\w+)/$', views.redirect_login, name='redirect_login'),
    url(r'^callback/$', views.callback, name='callback'),
    url(r'^callback-error/(?P<idp_alias>\w+)/$', views.callback_error, name='callback-error'),
    url(r'handle-login', views.handle_login, name="handle_login"),
    url(r'^logout$', views.start_logout, name='logout'),
    url(r'^verify-email/(?P<code>[\w-]+)/$', views.verify_email, name="verify_email"),
    url(r'^resend-email-link/', views.resend_email_link, name="resend_email_link"),
    url(r'^forgot-password/$', views.forgot_password, name="forgot_password"),
    url(r'^reset-password/(?P<code>[\w-]+)/$', views.reset_password, name="reset_password"),
]
