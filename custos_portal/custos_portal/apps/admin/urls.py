from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'custos_portal_admin'
urlpatterns = [
    url(r'^list-requests', views.list_new_tenant_requests, name='list_requests'),
    url(r'^request/(?P<tenant_request_id>[^/]+)/$', views.view_tenant_request, name="view_tenant_request"),
    url(r'^edit-tenant-request/(?P<tenant_request_id>[^/]+)/$', views.edit_tenant_request, name="edit_tenant_request")
]
