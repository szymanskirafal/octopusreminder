from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^new/$',
        view=views.ThingsNewCreateView.as_view(),
        name='new'
    ),
    url(
        regex=r'^list/$',
        view=views.ThingsListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^detail/(?P<pk>\d+)/$',
        view=views.ThingsDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^edit/(?P<pk>\d+)/$',
        view=views.ThingsEditUpdateView.as_view(),
        name='edit'
    ),
    url(
        regex=r'^thing-saved/$',
        view=views.ThingsThingSavedTemplateView.as_view(),
        name='saved'
    ),

]
