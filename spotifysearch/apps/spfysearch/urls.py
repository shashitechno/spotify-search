from django.conf.urls import url

from . import views

app_name = 'spfysearch'
urlpatterns = [
    url(r'^$', views.Search.as_view(), name='index'),
]
