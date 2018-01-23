from django.views import generic


class HowtoInstallTemplateView(generic.TemplateView):
    template_name = "howto/install.html"

class HowtoSignupTemplateView(generic.TemplateView):
    template_name = "howto/signup.html"
