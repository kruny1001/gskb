from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

# This is to make 404 and 500 error pages work despite a bug in django...
# URLs used:
# http://djangobook.com/en/1.0/appendixH/ (how to manually set handlers)
# http://stackoverflow.com/questions/3658659/why-cant-i-set-debug-false-in-my-django-app-on-dreamhost-without-getting-an-err
# (another solution, though it didn't work when I tried it)
handler404 =  'django.views.defaults.page_not_found'
handler500 =  'django.views.defaults.server_error'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bioinfo.views.home', name='home'),
    # url(r'^bioinfo/', include('bioinfo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),

    # Begin geneset stuff
    (r'^arapath/', include('bioinfo.genesets.urls')),
    (r'^geneflock/', include('bioinfo.genesets2.urls')),
)
