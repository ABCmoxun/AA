from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^01_request/$',request_views),
    url(r'^02_login/$',login_views),
]