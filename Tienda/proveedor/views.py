from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from .models import Proveedor
from .form import ProveedorForm
from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    DetailView
)

# Create your views here.
############################ VIEWS ####################################
class ProveedorListar(ListView):  #Listado de Proveedors
    model = Proveedor
    template_name = 'proveedor\listado.html'
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
    

class ProveedorCrear(CreateView): #Crear Proveedor
    model = Proveedor
    template_name = 'proveedor\crear.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor_app:listado_proveedores')

    def form_valid(self, form):
        proveedor = form.save(commit=False)
        proveedor.save()
        return super(ProveedorCrear, self).form_valid(form)
    
    
class ProveedorEditar(UpdateView): #Crear proveedor
    model = Proveedor
    form_class = ProveedorForm

    def form_valid(self, form):
        response = super().form_valid(form)

        self.object.save()

        return response
    
class ProveedorBorrar(View):
    def get(self, request, *args, **kwargs):
        proveedor  = get_object_or_404(Proveedor, pk=kwargs['pk'])
        proveedor.delete()
        return redirect('proveedor_app:listado_proveedores')
