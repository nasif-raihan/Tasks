from django.urls import path

from task_three.views import home, get_coordinates

urlpatterns = [
    path("", home, name="home"),
    path("get", get_coordinates, name="get_coordinates"),
]
