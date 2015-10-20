from django.conf.urls import url, patterns
from app import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^buy_ticket/$', views.buy_ticket, name='buy_ticket'),
    url(r'^tickets/$', views.tickets, name='tickets'),
)

