from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zhyblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^test/(\d+)$', 'zhyblog.views.test'),
    url(r'^bl$', 'zhyblog.views.bl'),

    url(r'^blog_update_save/(\d+)$', 'zhyblog.views.blog_update_save'),
    url(r'^blog_create$', 'zhyblog.views.blog_create'),
    url(r'^list$', 'zhyblog.views.blog_list'),
    url(r'^blog_update/(\d+)$', 'zhyblog.views.blog_update'),
    url(r'^blog_delete/(\d+)$', 'zhyblog.views.blog_delete'),

    url(r'^admin/', include(admin.site.urls)),
)
