from django.urls import path
from core_apps.account import views


app_name = "core_apps.account"

urlpatterns = [
    path("", views.account, name="account"),
    path("kyc-reg/", views.kyc_registration, name="kyc-reg"),
]