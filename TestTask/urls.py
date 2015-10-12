__author__ = 'kirillcherepanov'

from django.conf.urls import patterns, url
from TestTask import views


urlpatterns = patterns('',
    url(r'^$', views.login_page, name='login_page'),
    url(r'^validate_login/', views.validate_login_page, name='validate_login'),
    url(r'^scheme', views)

)