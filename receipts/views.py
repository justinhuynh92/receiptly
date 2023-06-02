from django.shortcuts import render, redirect
from receipts.models import Receipt, ExpenseCategory, Account
from django.contrib.auth.decorators import login_required
from receipts.forms import ReceiptForm, CategoryForm, AccountForm

# Create your views here.


@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts": receipts,
    }
    return render(request, "receipts/list.html", context)


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect('home')

    else:
        form = ReceiptForm()
    context = {
        "form": form,
    }
    return render(request, "receipts/create.html", context)

@login_required
def category_list(request):
    #filter by ONLY the current user from the models
    categories = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        "categories": categories,
    }
    return render(request, "categories/list.html", context)

@login_required
def account_list(request):
    #filter by ONLY the current user from the models
    accounts = Account.objects.filter(owner=request.user)
    context = {
        "accounts": accounts,
    }
    return render(request, "accounts/list.html", context)

@login_required
def create_category(request):
    #created new form
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            #owner must be set to current user
            category.owner = request.user
            category.save()
            #redirect the browser to the list of expense categories
        return redirect('category_list')
    else:
        form = CategoryForm()
    context = {
        "form": form,
    }
    return render(request, "categories/create.html", context)

@login_required
def create_account(request):
    #created new form
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            #owner must be set to current user
            category.owner = request.user
            category.save()
            #redirect the browser to the list of expense categories
        return redirect('account_list')
    else:
        form = CategoryForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/create.html", context)
