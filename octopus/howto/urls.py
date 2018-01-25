from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^install/$',
        view=views.HowtoInstallTemplateView.as_view(),
        name='install'
    ),
    url(
        regex=r'^pay/$',
        view=views.HowtoPayTemplateView.as_view(),
        name='pay'
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
