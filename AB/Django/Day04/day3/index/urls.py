from django.conf.urls import url
from .views import *
urlpatterns = [
    #http://localhost:8000/01_add/
    url(r'^01_add/$',add_views),
    #http://localhost:8000/02_query/
    url(r'^02_query/$',query_views),
    #http://localhost:8000/03_aulist/
    url(r'^03_aulist/$',aulist_views),
    #http://localhost:8000/04_delete/ID
    url(r'^04_delete/(\d+)/$',delete_views,name='del')
]