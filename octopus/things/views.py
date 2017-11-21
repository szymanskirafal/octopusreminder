from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ThingForm
from .models import Thing
from .tasks import task_printing


class ThingsNewCreateView(LoginRequiredMixin, generic.CreateView):
    model = Thing
    form_class = ThingForm
    template_name = 'things/new.html'
    context_object_name = 'thing'
    success_url = '/things/thing-saved/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        task_printing(self)
        #send_mail('email test', 'Just trying mailgun email', 'octopus@octopusreminder.com', ['r.szymansky@gmail.com'])
        return super(ThingsNewCreateView, self).form_valid(form)

class QueryCreatedByCurrentUserMixin(object):

    def get_queryset(self, *args, **kwargs):
        current_user = self.request.user
        queryset = Thing.objects.all().filter(created_by = current_user)
        return queryset

class ThingsListView(LoginRequiredMixin, QueryCreatedByCurrentUserMixin, generic.ListView):
    model = Thing
    template_name = 'things/list.html'
    context_object_name = 'things'


class ThingsDetailView(LoginRequiredMixin, QueryCreatedByCurrentUserMixin, generic.DetailView):
    model = Thing
    template_name = 'things/detail.html'
    context_object_name = 'thing'


class ThingsEditUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Thing
    form_class = ThingForm
    template_name = 'things/edit.html'
    context_object_name = 'thing'
    success_url = '/things/thing-saved/'

class ThingsThingSavedTemplateView(generic.TemplateView):
    template_name = 'things/thing-saved.html'

class ThingsDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Thing
    context_object_name = 'thing'
    success_url = reverse_lazy('things:list')
