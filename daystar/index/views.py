from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import BabyForm, PaymentForm, ProcurementItemForm, SitterForm
from .models import Sitter, Baby, Payment, ProcurementItem


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard upon successful login
        else:
            # Handle invalid login attempt
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


# Sitter Views
def sitter_list(request):
    sitters = Sitter.objects.filter(active=True)
    return render(request, 'sitter_list.html', {'sitters': sitters})

def sitter_detail(request, sitter_id):
    sitter = get_object_or_404(Sitter, pk=sitter_id)
    return render(request, 'sitter_detail.html', {'sitter': sitter})

def add_sitter(request):
    if request.method == 'POST':
        form = SitterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sitter added successfully.')
            return redirect('sitter_list')
    else:
        form = SitterForm()
    return render(request, 'add_sitter.html', {'form': form})

def edit_sitter(request, sitter_id):
    sitter = get_object_or_404(Sitter, pk=sitter_id)
    if request.method == 'POST':
        form = SitterForm(request.POST, instance=sitter)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sitter updated successfully.')
            return redirect('sitter_list')
    else:
        form = SitterForm(instance=sitter)
    return render(request, 'edit_sitter.html', {'form': form, 'sitter': sitter})

def delete_sitter(request, sitter_id):
    sitter = get_object_or_404(Sitter, pk=sitter_id)
    if request.method == 'POST':
        sitter.delete()
        messages.success(request, 'Sitter deleted successfully.')
        return redirect('sitter_list')
    return render(request, 'delete_sitter.html', {'sitter': sitter})

# Baby Views
def baby_list(request):
    babies = Baby.objects.all()
    return render(request, 'baby_list.html', {'babies': babies})

def baby_detail(request, baby_id):
    baby = get_object_or_404(Baby, pk=baby_id)
    return render(request, 'baby_detail.html', {'baby': baby})

def add_baby(request):
    if request.method == 'POST':
        form = BabyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Baby added successfully.')
            return redirect('baby_list')
    else:
        form = BabyForm()
    return render(request, 'add_baby.html', {'form': form})

def edit_baby(request, baby_id):
    baby = get_object_or_404(Baby, pk=baby_id)
    if request.method == 'POST':
        form = BabyForm(request.POST, instance=baby)
        if form.is_valid():
            form.save()
            messages.success(request, 'Baby updated successfully.')
            return redirect('baby_list')
    else:
        form = BabyForm(instance=baby)
    return render(request, 'edit_baby.html', {'form': form, 'baby': baby})

def delete_baby(request, baby_id):
    baby = get_object_or_404(Baby, pk=baby_id)
    if request.method == 'POST':
        baby.delete()
        messages.success(request, 'Baby deleted successfully.')
        return redirect('baby_list')
    return render(request, 'delete_baby.html', {'baby': baby})

# Payment Views
def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment_list.html', {'payments': payments})

def payment_detail(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    return render(request, 'payment_detail.html', {'payment': payment})

def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Payment recorded successfully.')
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'add_payment.html', {'form': form})

def edit_payment(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Payment updated successfully.')
            return redirect('payment_list')
    else:
        form = PaymentForm(instance=payment)
    return render(request, 'edit_payment.html', {'form': form, 'payment': payment})

def delete_payment(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    if request.method == 'POST':
        payment.delete()
        messages.success(request, 'Payment deleted successfully.')
        return redirect('payment_list')
    return render(request, 'delete_payment.html', {'payment': payment})

# ProcurementItem Views
def procurement_list(request):
    procurement_items = ProcurementItem.objects.all()
    return render(request, 'procurement_list.html', {'procurement_items': procurement_items})

def procurement_detail(request, procurement_item_id):
    procurement_item = get_object_or_404(ProcurementItem, pk=procurement_item_id)
    return render(request, 'procurement_detail.html', {'procurement_item': procurement_item})

def add_procurement_item(request):
    if request.method == 'POST':
        form = ProcurementItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Procurement item added successfully.')
            return redirect('procurement_list')
    else:
        form = ProcurementItemForm()
    return render(request, 'add_procurement_item.html', {'form': form})

def edit_procurement_item(request, procurement_item_id):
    procurement_item = get_object_or_404(ProcurementItem, pk=procurement_item_id)
    if request.method == 'POST':
        form = ProcurementItemForm(request.POST, instance=procurement_item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Procurement item updated successfully.')
            return redirect('procurement_list')
    else:
        form = ProcurementItemForm(instance=procurement_item)
    return render(request, 'edit_procurement_item.html', {'form': form, 'procurement_item': procurement_item})

def delete_procurement_item(request, procurement_item_id):
    procurement_item = get_object_or_404(ProcurementItem, pk=procurement_item_id)
    if request.method == 'POST':
        procurement_item.delete()
        messages.success(request, 'Procurement item deleted successfully.')
        return redirect('procurement_list')
    return render(request, 'delete_procurement_item.html', {'procurement_item': procurement_item})
