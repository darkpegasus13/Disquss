from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


app_name = 'login_page'
urlpatterns = [
    url(r'^SbDate/$', views.index_date, name='sbd'),
    url(r'^SbReply/$', views.index_replies, name='sbr'),
    url(r'^SbUnans/$', views.index_unanswered, name='sbu'),
    url(r'^SbTrend/$', views.index_trending, name='sbt'),
    url(r'^SbCate/$', views.index_categories, name='sbc'),
    url(r'^Search/$', views.search, name='search'),
    url(r'^$', views.index, name='index'),
    url(r'^Logout/$', auth_views.logout, {'template_name': 'login_page/Login.html'}, name='logout'),
    url(r'^Login/$', views.login_user, name='login'),
    url(r'^Register/$', views.register, name="register"),
    url(r'^Profile/$', views.profile, name="profile"),
]
