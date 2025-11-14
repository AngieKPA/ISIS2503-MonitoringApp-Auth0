from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ProductForm
from .logic.product_logic import get_products, create_product
from django.contrib.auth.decorators import login_required
from monitoring.auth0backend import getRole

@login_required
def product_list(request):
    role = getRole(request)
    allowed = {"Administrador", "SupervisorLogístico", "AuditorInterno"}
    if role not in allowed:
        messages.error(request, "No tiene permisos para ver productos.")
        return HttpResponseRedirect(reverse('index'))
    products = get_products()
    return render(request, 'products/product_list.html', {'products': products})

@login_required
def product_create(request):
    role = getRole(request)
    if role not in {"Administrador", "SupervisorLogístico"}:
        messages.error(request, "No tiene permisos para crear productos.")
        return HttpResponseRedirect(reverse('products'))
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            create_product(form.cleaned_data)
            messages.success(request, "Producto creado.")
            return HttpResponseRedirect(reverse('products'))
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})
