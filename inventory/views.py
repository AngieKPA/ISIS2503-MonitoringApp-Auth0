from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import StockItemForm
from .logic.inventory_logic import get_stock_items, create_stock_item
from django.contrib.auth.decorators import login_required
from monitoring.auth0backend import getRole

@login_required
def inventory_list(request):
    role = getRole(request)
    # Lectura de inventario: todos menos restricciones severas
    allowed = {"Administrador", "SupervisorLogístico", "OperarioBodega", "VerificadorCalidad", "AuditorInterno"}
    if role not in allowed:
        messages.error(request, "No tiene permisos para ver inventario.")
        return HttpResponseRedirect(reverse('index'))
    stock_items = get_stock_items()
    return render(request, 'inventory/inventory_list.html', {'stock_items': stock_items})

@login_required
def inventory_create(request):
    role = getRole(request)
    # Crear entradas: Operario, Supervisor, Admin
    if role not in {"OperarioBodega", "SupervisorLogístico", "Administrador"}:
        messages.error(request, "No tiene permisos para registrar entradas.")
        return HttpResponseRedirect(reverse('inventory'))
    if request.method == 'POST':
        form = StockItemForm(request.POST)
        if form.is_valid():
            create_stock_item(form.cleaned_data)
            messages.success(request, "Entrada de inventario registrada.")
            return HttpResponseRedirect(reverse('inventory'))
    else:
        form = StockItemForm()
    return render(request, 'inventory/inventory_form.html', {'form': form})
