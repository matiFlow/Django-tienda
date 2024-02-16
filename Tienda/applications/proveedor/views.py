from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from .models import Proveedor
from .form import ProveedorForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    DetailView
)
@method_decorator(login_required, name='dispatch')
# Create your views here.
############################ VIEWS ####################################
class ProveedorListar(ListView, LoginRequiredMixin):  #Listado de Proveedors
    model = Proveedor
    template_name = 'proveedor/listado.html'
    context_object_name = "lista"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        print("Total de elementos:", queryset.count())
        searchByName = self.request.GET.get("name")
        searchBySurname = self.request.GET.get("surname")
        searchByTelefono = self.request.GET.get("telefono")

        if searchByName:
            queryset = queryset.filter(nombre__icontains=searchByName).distinct()
        
        if searchBySurname:
            queryset = queryset.filter(apellido__icontains=searchBySurname).distinct()
        
        if searchByTelefono:
            queryset = queryset.filter(telefono__icontains=searchByTelefono).distinct()
        
        queryset = queryset.order_by('nombre')
            
        return queryset
    

class ProveedorCrear(CreateView, LoginRequiredMixin): #Crear Proveedor
    model = Proveedor
    template_name = 'proveedor/crear.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor_app:listado_proveedores')

    def form_valid(self, form):
        proveedor = form.save(commit=False)
        proveedor.save()
        messages.success(self.request, 'Registro guardado con éxito')
        return super(ProveedorCrear, self).form_valid(form)
    
    
class ProveedorEditar(UpdateView, LoginRequiredMixin): #Crear proveedor
    model = Proveedor
    template_name = 'proveedor/editar.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor_app:listado_proveedores')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object 
        return kwargs

    def form_valid(self, form):
        cliente = form.save(commit=False)
        cliente.save()
        messages.success(self.request, 'Operacion realizada con éxito')
        return super(ProveedorEditar, self).form_valid(form)
    
class ProveedorBorrar(DeleteView, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        proveedor  = get_object_or_404(Proveedor, pk=kwargs['pk'])
        proveedor.delete()
        return redirect('proveedor_app:listado_proveedores')

class ProveedorDetalles(DetailView, LoginRequiredMixin): 
    model = Proveedor
    template_name = "proveedor/detalle.html"
    context_object_name = "detalle"
    login_url = reverse_lazy('proveedor_app:listado_proveedores')