from django.conf.urls import url

from . import views

app_name = 'mypats'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<duration>[0-9]+)$', views.index_duration, name='index_duration'),
    url(r'^api/(?P<duration>[0-9]+)/$', views.api, name='api'),
    url(r'^api/$', views.api_all, name='api_all'),
    url(r'^stats/age$', views.stats_age, name='stats_age'),
    url(r'^stats/sex$', views.stats_sex, name='stats_sex'),
    url(r'^stats/address$', views.stats_address, name='stats_address'),
    url(r'^stats/date$', views.stats_date, name='stats_date'),
    url(r'^stats/$', views.stats, name='stats'),
]