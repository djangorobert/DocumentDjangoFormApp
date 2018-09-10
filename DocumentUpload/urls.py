from django.conf.urls import url
from DocumentUpload import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^upload/$', views.upload, name='upload'),
]
