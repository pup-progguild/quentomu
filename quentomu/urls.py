from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'quentomu.views.home', name='home'),
    url(r'^conversations$', 'quentomu.views.conversation', name='conversation'),
    url(r'^topics$', 'quentomu.views.topics', name='topics'),

    url(r'^topics/(?P<id>\d+)$', 'quentomu.views.topics_show',
    	name='topics_show'),
    url(r'^topics/(?P<id>\d+)/create$', 'quentomu.views.topics_create',
    	name='topics_create'),
    url(r'^topics/reply/(?P<id>\d+)$', 'quentomu.views.topics_reply',
    	name='topics_reply'),

    url(r'^distance/(?P<user1_id>\d+)/(?P<user2_id>\d+)', 'quentomu.views.distance',
    	name='distance'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #pols
    url(r'^testDN/(?P<number>\d+)/(?P<msg>.*)$', 'quentomu.views.DeliveryNotif',name = 'DelivNotif'),
    url(r'^testInbox/$', 'quentomu.views.ReceivedMsgs',name = 'ReceiveMsgs'),
    url(r'^testSendMoney/$','quentomu.views.Remittance',name = 'Remittance'),
]
