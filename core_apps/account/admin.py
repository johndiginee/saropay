from django.contrib import admin
from core_apps.account.models import Account
from core_apps.userauths.models import User
from import_export.admin import ImportExportModelAdmin


class AccountAdminModel(ImportExportModelAdmin):
    list_editable = ['account_status', 'account_balance']
    list_display = ['user', 'account_number' ,'account_status', 'account_balance', 'kyc_submitted', 'kyc_confirmed']
    list_filter = ['account_status']

# class KYCAdmin(ImportExportModelAdmin):
#     model = Account
#     search_fields = ["full_name"]
#     list_display = ['user', 'full_name']

admin.site.register(Account, AccountAdminModel)