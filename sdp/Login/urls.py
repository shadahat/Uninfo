######### Author :  Noboni + Shahin  + Nowshad #########

from django.conf.urls import url
from . import views


from django.contrib.auth import views as auth_views
from .views import home
urlpatterns = [

    url(r'^$', views.index.as_view() , name='index'),
        url(r'^loginn/$',views.LoginRequest.as_view(),name='Login'),
            url(r'^(?P<pk>[0-9]+)/$',views.UpdateProfile.as_view(),name='update'),
    url(r'^search/universitysearch/$', views.UniversitySearch.as_view(), name='universitysearch'),
    url(r'^search/depatmentsearch/(?P<pk>[0-9]+)/$', views.departmentbasesearch.as_view(), name='departmentsearch'),
    url(r'^search/collegesearch/$', views.Collegesearch.as_view(), name='collegesearch'),
    url(r'^search/collegesearch/(?P<pk>[0-9]+)/$', views.cnamesearch.as_view(), name='collegestudents'),
    url(r'^search/schoolsearch/$', views.Schoolsearch.as_view(), name='schoolsearch'),
    url(r'^search/schoolsearch/(?P<pk>[0-9]+)/$', views.snamesearch.as_view(), name='schoolstudents'),
    url(r'^search/namesearch/(?P<pk>[0-9]+)/$', views.unamesearch.as_view(), name='unamesearch'),
    url(r'^search/basicprofile/(?P<pk>[0-9]+)/$', views.basicprofile.as_view(), name='namesearch'),





    url(r'^linkedinupdate/$', home, name='home'),
    url(r'^$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

]

