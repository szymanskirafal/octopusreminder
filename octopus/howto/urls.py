from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^use/$',
        view=views.HowtoUseTemplateView.as_view(),
        name='use'
    ),
    url(
        regex=r'^install/$',
        view=views.HowtoInstallTemplateView.as_view(),
        name='install'
    ),
    url(
        regex=r'^price/$',
        view=views.HowtoPriceTemplateView.as_view(),
        name='price'
    ),
    url(
        regex=r'^signup/$',
        view=views.HowtoSignupTemplateView.as_view(),
        name='signup'
    ),
    url(
        regex=r'^signin/$',
        view=views.HowtoSigninTemplateView.as_view(),
        name='signin'
    ),


]
