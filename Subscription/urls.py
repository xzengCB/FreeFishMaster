from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<subID>[0-9]{1,11})$', views.index, name='delete'),
]