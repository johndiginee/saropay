from django.urls import path
from core_apps.core import views


app_name = "core_apps.core"

urlpatterns = [
    path("", views.index, name="index"),
]