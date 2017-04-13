from django.conf.urls import include, url

from spotifysearch.apps.spfysearch import urls as spotify_urls

urlpatterns = [
	url(r'^', include(spotify_urls, namespace='index')),
]
