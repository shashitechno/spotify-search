
from .utils import search_index


from django.views.generic import TemplateView

# This variable maps a search type to the name of the key containing search
# results. It's immutable because it should change - the Spotify API _should_
# be stable.


class Search(TemplateView):

    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        return search_index(request)

    def post(self, request, *args, **kwargs):
        return search_index(request)