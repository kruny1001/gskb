from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bioinfo.views.home', name='home'),
    # url(r'^bioinfo/', include('bioinfo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),

    # Begin geneset stuff

    (r'^genesets/set/(\w+)/$', 'bioinfo.genesets.views.geneset'),
    #(r'^genesets/$', (geneset search page)),
)
