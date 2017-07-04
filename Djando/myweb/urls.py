from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^home/', views.index),
    url(r'^add/', views.add),
    url(r'^show/', views.show)
 ]