from django.shortcuts import render, redirect
from core_apps.account.models import Account
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages

from core_apps.core.models import Transaction

@login_required
def search_users_account_number(request):
    account = Account.objects.all()
    query = request.POST.get("account_number")
    if query:
        account = account.filter(
            Q(account_number=query)|
            Q(account_id=query)
        ).distinct()

    context = {
        "account": account,
        "query": query,
    }
    return render(request, "transfer/search-user-account-number.html", context)

def AmountTransfer(request, account_number):
    try:
        account = Account.objects.get(account_number=account_number)
    except:
        messages.warning(request, "Account does not exist.")
        return redirect("core_apps.core:search-account")
    context = {
        "account": account,
    }
    return render(request, "transfer/amount-transfer.html", context)

def AmountTransferProcess(request, account_number):
    account = Account.objects.get(account_number=account_number) ## get the sender's account
    sender = request.user # get the person that is logged in
    reciever = account.user # get the reciever account

    sender_account = request.user.account # get the currently logged in users account
    receiver_account = account # get the recievers account 

    if request.method == "POST":
        amount = request.POST.get("amount-send")
        description = request.POST.get("description")

        print(amount)
        print(description)

        if sender_account.account_balance > 0 and amount:
            """Check avaliable funds, and create new transaction."""
            new_transaction = Transaction.objects.create(
                user=request.user,
                amount=amount,
                description=description,
                receiver=reciever,
                sender=sender,
                sender_account=sender_account,
                receiver_account=receiver_account,
                status="processing",
                transaction_type="transfer"
            )
            new_transaction.save() # save transaction
            
            # get the id of the recent transaction
            transaction_id = new_transaction.transaction_id

            return redirect("core_apps.core:transfer-confirmation", account.account_number, transaction_id)
        else:
            messages.warning(request, "Insufficent fund.")
            return redirect("core_apps.core:amount-transfer", account.account_number)
    else:
        messages.warning(request, "Error Occured, Try again.")
        return redirect("core_apps.account:account")


def TransferConfirmation(request, account_number, transaction_id):
    try:
        account = Account.objects.get(account_number=account_number)
        transaction = Transaction.objects.get(transaction_id=transaction_id)
    except:
        messages.warning(request, "Transaction doesn't exist.")
        return redirect("core_apps.account:account")

    context = {
        "account": account,
        "transaction": transaction,
    }
    return render(request, "transfer/transfer-confirmation.html", context)