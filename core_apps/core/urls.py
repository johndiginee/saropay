from django.urls import path
from core_apps.core import views
from core_apps.core import transfer



app_name = "core_apps.core"

urlpatterns = [
    path("", views.index, name="index"),

    # Transfer
    path("search-account/", transfer.search_users_account_number, name="search-account"),

]