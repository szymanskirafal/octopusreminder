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

class ThingsListView(LoginRequiredMixin, generic.ListView):
    model = Thing
    template_name = 'things/list.html'
    context_object_name = 'things'

    def get_queryset(self, *args, **kwargs):
        current_user = self.request.user
        queryset = Thing.objects.all().filter(created_by = current_user)
        return queryset

class ThingsDetailView(LoginRequiredMixin, generic.DetailView):
    model = Thing
    template_name = 'things/detail.html'
    context_object_name = 'thing'
    

class ThingsThingSavedTemplateView(generic.TemplateView):
    template_name = 'things/thing-saved.html'
