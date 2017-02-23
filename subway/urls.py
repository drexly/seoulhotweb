from django.conf.urls import url, include
from .views import SubwayLV, subway_lazy, subway_now,main,bsbusy,bsempty,bsmy,bsvs,bscm,bsfd,bsch,bssh,source

app_name='subway'
urlpatterns = [
    url(r'^$', main, name='index'),
    url(r'busy/$', SubwayLV, name='busy'),
    url(r'lazy/$', subway_lazy, name='lazy'),
    url(r'now/$', subway_now, name='now'),

    url(r'1bz/$', bsbusy, name='1bz'),
    url(r'2em/$', bsempty, name='2em'),
    url(r'3my/$', bsmy, name='3my'),
    url(r'4vs/$', bsvs, name='4vs'),
    url(r'5cm/$', bscm, name='5vs'),
    url(r'6fd/$', bsfd, name='6fd'),
    url(r'chat/$', bsch, name='chat'),
    url(r'search/$', bssh, name='search'),
    url(r'2014/$', source, name='src'),
]
