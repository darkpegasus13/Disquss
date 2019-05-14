from django.conf.urls import url
from . import views

app_name = 'thread'
urlpatterns = [
    url(r'^$', views.Thread.as_view(), name='posting'),
    url(r'^answer/(?P<pk>\d+)/$', views.Answer.as_view(), name='answer'),
    url(r'^Like/$', views.like_post, name='like_post'),
    url(r'^Comment/$', views.comment, name='comment')
    ]
