from django.conf.urls import patterns, include, url
from ToDoProject import views
from django.contrib.auth.views import login

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


# Examples:
# url(r'^$', 'CodeScoutsProject.views.home', name='home'),
# url(r'^CodeScoutsProject/', include('CodeScoutsProject.foo.urls')),

# Uncomment the admin/doc line below to enable admin documentation:
#url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

# Uncomment the next line to enable the admin:
urlpatterns = patterns('',
    url(r'^$', views.welcome, name='welcome'),
    #url(r'^login/$', views.login_view),
    url(r'^login/$', login, {'template_name': 'auth.html'}),
    url(r'^logout/$', views.logout_view),
    url(r'^accounts/profile/$', views.profile, name="profile"),
    url(r'^admin/', include(admin.site.urls)),
)


