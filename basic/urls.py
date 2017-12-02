from django.conf.urls import url
from . import views
from .feeds import NewsFeed

app_name = 'basic'

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^adddetails/$', views.adddetails, name='adddetails'),
    url(r'^search/$', views.search, name='query'),
    url(r'^logout/$', views.logOut, name='logout'),
    url(r'^feedback/$', views.feeds, name='feed'),
    url(r'^addmusic/$',views.addobject,name='addmusic'),
    url(r'^addmovie/$',views.addobject,name='addmovie'),
    url(r'^message/$', views.addobject, name='message'),
    url(r'^message/(?P<id>[0-9]+)/$', views.addobject, name='messagewithdata'),
    url(r'^inbox/$', views.inbox, name='inbox'),
    url(r'^delmessage/(?P<id>[0-9]+)$',views.delete, name='delmessage' ),
    url(r'^profile/(?P<user>.*)$', views.profile, name='profile'),
    url(r'^post/$', views.post, name='post'),
    url(r'^like/(?P<content>[A-Za-z0-9]+)/(?P<id>[0-9]+)', views.like, name='like'),
    url(r'^latestfeeds/$', NewsFeed()),
    url(r'^addbook/$', views.addobject, name='addbook'),
    url(r'^feeds/(?P<id>[0-9]+)/', views.comment, name='comment'),
]