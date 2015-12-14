from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
                       url(r'^categories/(?P<id>\d+)/$', views.one_category, name= 'by_category'),
                       url(r'^product/(?P<id>\d+)/$', views.product, name='product'),
                       url(r"^page/(\d+)/$", views.index),
                       url(r'^$', views.index),
                       url(r'^cart/$', views.cart, name='cart'),
                       url(r'^add_comment/(?P<id>\d+)/$', views.add_comment),
                       url(r'^search/$', views.search , name='search'),
                       url(r'^add_to_cart/(?P<id>\d+)/$', views.add_to_cart , name='add_to_card'),
                       url(r'^del_from_cart/(?P<id>\d+)/$', views.del_from_cart , name='del'),
                       url(r'^order/$', views.order , name='order'),
                       )
