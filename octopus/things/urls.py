from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^new/$',
        view=views.ThingsNewCreateView.as_view(),
        name='new'
    ),
    
]
