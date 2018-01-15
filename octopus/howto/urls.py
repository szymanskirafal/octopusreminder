from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^install/$',
        view=views.HowtoInstallTemplateView.as_view(),
        name='install'
    ),


]
