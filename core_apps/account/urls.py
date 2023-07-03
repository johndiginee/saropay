from django.urls import path
from core_apps.account import views


app_name = "core_apps.userauths"

urlpatterns = [
    path("kyc-reg/", views.kyc_registration, name="kyc-reg"),
]