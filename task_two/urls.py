from django.urls import path
from .views import add_data, retrieve_data, update_data, delete_data, home

urlpatterns = [
    path("", home, name="home"),
    path("add", add_data, name="add"),
    path("retrieve", retrieve_data, name="retrieve"),
    path("update/<int:uid>", update_data, name="update"),
    path("delete/<int:uid>", delete_data, name="delete"),
]
