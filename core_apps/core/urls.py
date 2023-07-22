from django.urls import path
from core_apps.core import views
from core_apps.core import transfer
from core_apps.core import transaction



app_name = "core_apps.core"

urlpatterns = [
    path("", views.index, name="index"),

    # Transfer
    path("search-account/", transfer.search_users_account_number, name="search-account"),
    path("amount-transfer/<account_number>/", transfer.AmountTransfer, name="amount-transfer"),
    path("amount-transfer-process/<account_number>/", transfer.AmountTransferProcess, name="amount-transfer-process"),
    path("transfer-confirmation/<account_number>/<transaction_id>/", transfer.TransferConfirmation, name="transfer-confirmation"),
    path("transfer-process/<account_number>/<transaction_id>/", transfer.TransferProcess, name="transfer-process"),
    path("transfer-completed/<account_number>/<transaction_id>/", transfer.TransferComplete, name="transfer-completed"),

    # Transactions
    path("transactions/", transaction.transaction_lists, name="transactions"),
    path("transaction-detail/<transaction_id>", transaction.transaction_detail, name="transaction-detail"),
]