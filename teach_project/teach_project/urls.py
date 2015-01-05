from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings  #allows us to access variables defined within our project's settings.py file

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teach_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^categories/',include('categories.urls')) #Added categories app url to project's url
)

if settings.DEBUG:  #the conditional statements check if our django project is run in DEBUG MODE (understand that DEBUG is false in deployment)
    urlpatterns+=patterns(
                           'django.views.static',
                           (r'^media/(?P<path>.*)',
                            serve,
                            {'document_root':settings.MEDIA_ROOT}), )
''' If debug is true, additional url pattern is added to urlpatterns tuple. 
    The pattern states that for any file requested with a URL starting with media/,
    the request will be passed to django.views.static view. This view handles 
    the dispatching of uploaded media files for you'''
