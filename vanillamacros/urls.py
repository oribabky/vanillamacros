from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(\w+)/$', views.wowClass, name='class'),
    url(r'^(\w+)/(\w+)/$', views.index, name='ability'),

]