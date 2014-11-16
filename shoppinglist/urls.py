from django.conf.urls import patterns, url

from shoppinglist import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # url(r'^blog/', include('blog.urls')),
)
