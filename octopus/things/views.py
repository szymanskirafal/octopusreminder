from django.core.urlresolvers import reverse
from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Thing


class ThingsNewCreateView(generic.CreateView):
    model = Thing
    fields = ['text']
    template_name = 'things/new.html'
    # These next two lines tell the view to index lookups by username
    #slug_field = 'username'
    #slug_url_kwarg = 'username'
