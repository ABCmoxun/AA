from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^01_request/$',request_views),
    url(r'^02_login/$',login_views),
    url(r'^03_get/',get_views),
    url(r'^04_query/',query_views),
    url(r'^05_form/$',form_views),
    url(r'^06_register/$',register_views),
    url(r'^07_modelForm/$',modelForm_views),
]