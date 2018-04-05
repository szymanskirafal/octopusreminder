from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin

from datetime import date

from .forms import ThingForm
from .models import Thing

class UserLoginRequiredAndPaidMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not request.user.paid:
            when_user_signed_up = request.user.created
            days_to_use_the_app_for_free = timedelta(days=1)
            today = date.today()
            if today - when_user_signed_up > days_to_use_the_app_for_free:
                return redirect('home')
        return super().dispatch(request, *args, **kwargs)



class ThingsNewCreateView(UserLoginRequiredAndPaidMixin, generic.CreateView):
    model = Thing
    form_class = ThingForm
    template_name = 'things/new.html'
    context_object_name = 'thing'
    success_url = '/things/list/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(ThingsNewCreateView, self).form_valid(form)

class QueryCreatedByCurrentUserMixin(object):

    def get_queryset(self, *args, **kwargs):
        current_user = self.request.user
        queryset = Thing.objects.all().filter(created_by = current_user)
        return queryset

class ThingsListView(UserLoginRequiredAndPaidMixin, QueryCreatedByCurrentUserMixin, generic.ListView):
    model = Thing
    template_name = 'things/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        context['today_things'] = queryset.filter(today = True)
        context['later_things'] = queryset.filter(today = False)
        return context



class ThingsDetailView(UserLoginRequiredAndPaidMixin, QueryCreatedByCurrentUserMixin, generic.DetailView):
    model = Thing
    template_name = 'things/detail.html'
    context_object_name = 'thing'


class ThingsEditUpdateView(UserLoginRequiredAndPaidMixin, generic.edit.UpdateView):
    model = Thing
    form_class = ThingForm
    template_name = 'things/edit.html'
    context_object_name = 'thing'
    success_url = '/things/list/'

class ThingsThingSavedTemplateView(generic.TemplateView):
    template_name = 'things/thing-saved.html'

class ThingsDeleteView(UserLoginRequiredAndPaidMixin, generic.edit.DeleteView):
    model = Thing
    context_object_name = 'thing'
    success_url = reverse_lazy('things:list')
