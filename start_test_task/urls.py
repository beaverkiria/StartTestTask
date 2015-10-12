from django.conf.urls import patterns, include, url
from django.contrib import admin
from TestTask import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'start_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.redirect_to_test_task),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^testtask/', include('TestTask.urls'))
)
