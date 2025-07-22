# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ExpenseForm
from .models import Expense
import json
from django.http import JsonResponse

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'home.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    
    # For Pie Chart
    category_totals = {}
    for expense in expenses:
        category_totals[expense.category] = category_totals.get(expense.category, 0) + float(expense.amount)

    # For Line Chart
    daily_totals = {}
    for expense in expenses:
        date_str = expense.date.strftime('%Y-%m-%d')
        daily_totals[date_str] = daily_totals.get(date_str, 0) + float(expense.amount)

    return render(request, 'dashboard.html', {
        'expenses': expenses,
        'category_data': json.dumps(category_totals),
        'trend_data': json.dumps(daily_totals),
    })

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.user = request.user
            exp.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

@login_required
def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id, user=request.user)
    expense.delete()
    return redirect('dashboard')
