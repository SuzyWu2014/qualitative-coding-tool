from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^codes/add$', views.add_code, name='add_code'),
]
