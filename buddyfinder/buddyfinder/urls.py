from django.conf.urls import include, url
from django.contrib import admin

from lists import views

urlpatterns = [
    url(r'^polls/', include('polls.urls',  namespace="polls")),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_page, name = "home"),
]
