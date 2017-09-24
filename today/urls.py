from django.conf.urls import url

from today import views

urlpatterns = [
    url(r'^$', views.get_today_celebrate),
    url(r'^raw/$', views.get_raw_today_celebrate),
]
