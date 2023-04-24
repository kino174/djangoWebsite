from . import views
from django.urls import path

urlpatterns=[
    path("",views.home, name="home"),
    path("resume/resume",views.resume, name="resume"),
]