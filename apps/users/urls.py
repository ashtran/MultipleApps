from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register$', views.new),
    url(r'^login$', views.show),
    url(r'^users/new$', views.new),
    url(r'^users$', views.index),
]
