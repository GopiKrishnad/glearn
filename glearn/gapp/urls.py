from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    #url(r'^soap$', views.my_soap_service),
    url(r'^dispatcher_handler$', views.dispatcher_handler),

]
