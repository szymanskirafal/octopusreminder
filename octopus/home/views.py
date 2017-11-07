from django.shortcuts import redirect
from django.views import generic

class HomeTemplateView(generic.TemplateView):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('things:new')
        else:
            return super(HomeTemplateView, self).get(request, *args, **kwargs)
