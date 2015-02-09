from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Eric.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$','spots.views.index',name='index'),

    url(r'^SpotSearch/$','spots.views.spotsearch',name='spotsearch'),

    url(r'^AboutInfo/$','spots.views.aboutinfo',name='aboutinfo'),
    
    url(r'^ContactInfo/$','spots.views.contactinfo',name='contactinfo'),

    url(r'^(?P<city_name>\w+)/$','spots.views.choosecity',name='choosecity'),

    url(r'^(?P<city_name>\w+)/(?P<zone_name>\w+)/$','spots.views.citydetails',name='citydetails'),

)
