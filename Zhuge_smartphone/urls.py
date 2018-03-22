from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^smartphone/(?P<smartphone_index>[0-9]+)/$', views.check_smartphone),
    url(r'^smartphone/(?P<smartphone_index>[0-9]+)/release/$', views.release_smartphone),
    url(r'^smartphone/(?P<smartphone_index>[0-9]+)/subscribe/$', views.subscribe_smartphone),
    url(r'^smartphone/(?P<smartphone_index>[0-9]+)/value/$', views.getPhoneValue),
    url(r'^smartphone/(?P<smartphone_index>[0-9]+)/(?P<shake_value>[0-9]+)/update/$', views.update_shake),
    url(r'^smartphone/shake/$', views.getShakeValue),
    url(r'^smartphone/releaseall/$', views.release_all),
    url(r'^smartphone/playernum/$', views.getOnlinePlayerNum),

]