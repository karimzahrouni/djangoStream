
from django.conf.urls import url
from django.contrib import admin
from .import views

# url patterns for browsing 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^/(?P<stream_path>(.*?))/$',views.dynamic_stream,name="videostream"),  
    url(r'^stream/$',views.indexscreen),
   ]
