from django.views import generic


class HowtoInstallTemplateView(generic.TemplateView):
    template_name = "howto/install.html"

class HowtoPriceTemplateView(generic.TemplateView):
    template_name = "howto/price.html"

class HowtoSignupTemplateView(generic.TemplateView):
    template_name = "howto/signup.html"

class HowtoSigninTemplateView(generic.TemplateView):
    template_name = "howto/signin.html"

class HowtoUseTemplateView(generic.TemplateView):
    template_name = "howto/use.html"
