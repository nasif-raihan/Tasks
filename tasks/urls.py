from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("task_two/", include("task_two.urls")),
    path("task_three/", include("task_three.urls")),
]
