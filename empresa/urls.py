from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.principal, name='principal'),
    url(r'^delete/', views.delete, name='delete'),
    url(r'^clasificacion/', views.clasificacion, name='clasificacion'),
    url(r'^principal/', views.principal, name='principal'),
]
