from django.views import generic


class HowtoInstallTemplateView(generic.TemplateView):
    template_name = "howto/install.html"

class HowtoPayTemplateView(generic.TemplateView):
    template_name = "howto/pay.html"

class HowtoSignupTemplateView(generic.TemplateView):
    template_name = "howto/signup.html"

class HowtoSigninTemplateView(generic.TemplateView):
    template_name = "howto/signin.html"
