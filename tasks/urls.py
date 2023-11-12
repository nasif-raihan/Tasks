from django.contrib import admin
from django.urls import path, include

from task_two.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("task_two/", include("task_two.urls")),
    path("task_three/", include("task_three.urls")),
]
