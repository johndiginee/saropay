from django.shortcuts import render, redirect
from core_apps.account.models import KYC, Account
from core_apps.account.forms import KYCForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def account(request):
    if request.user.is_authenticated:
        try:
            kyc = KYC.objects.get(user=request.user)
        except:
            messages.warning(request, "You need to submit your KYC.")
            return redirect("core_apps.account:kyc-reg")

        account = Account.objects.get(user=request.user)
    else:
        messages.warning(request, "You need to login to dashboard.")
        return redirect("core_apps.userauths:sign-in")
    context = {
        "kyc": kyc,
        "account": account,
    }
    return render(request, "account/account.html", context)

@login_required
def kyc_registration(request):
    user = request.user
    account = Account.objects.get(user=user)

    try:
        kyc = KYC.objects.get(user=user)
    except:
        kyc = None
    
    if request.method == "POST":
        form = KYCForm(request.POST, request.FILES, instance=kyc)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.account = account
            new_form.save()
            messages.success(request, "KYC Form submitted successfully, In review now.")
            return redirect("core_apps.core:index")
    else:
        form = KYCForm(instance=kyc)
    context = {
        "account": account,
        "form": form,
        "kyc": kyc,
    }
    return render(request, "account/kyc-form.html", context)

def dashboard(request):
    if request.user.is_authenticated:
        try:
            kyc = KYC.objects.get(user=request.user)
        except:
            messages.warning(request, "You need to submit your KYC.")
            return redirect("core_apps.account:kyc-reg")

        account = Account.objects.get(user=request.user)
    else:
        messages.warning(request, "You need to login to dashboard.")
        return redirect("core_apps.userauths:sign-in")
    
    context = {
        "kyc": kyc,
        "account": account,
    }
    return render(request, "account/dashboard.html", context)
