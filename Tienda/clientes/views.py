from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from .models import Cliente
from .form import ClienteForm
from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    DetailView
)

# Create your views here.
############################ VIEWS ####################################
class ClienteListar(ListView):  #Listado de clientes
    model = Cliente
    template_name = 'cliente\listado.html'
    context_object_name = "lista"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        print("Total de elementos:", queryset.count())
        searchByName = self.request.GET.get("name")
        searchBySurname = self.request.GET.get("surname")
        searchByDni = self.request.GET.get("dni")

        if searchByName:
            queryset = queryset.filter(nombre__icontains=searchByName).distinct()
        
        if searchBySurname:
            queryset = queryset.filter(apellido__icontains=searchBySurname).distinct()
        
        if searchByDni:
            queryset = queryset.filter(dni__icontains=searchByDni).distinct()
        
        queryset = queryset.order_by('nombre')
            
        return queryset
    

class ClienteCrear(CreateView): #Crear cliente
    model = Cliente
    template_name = 'cliente\crear.html'
    form_class = ClienteForm
    success_url = reverse_lazy('cliente_app:listado_clientes')

    def form_valid(self, form):
        cliente = form.save(commit=False)
        cliente.save()
        return super(ClienteCrear, self).form_valid(form)
    
    
class ClienteEditar(UpdateView): #Crear cliente
    model = Cliente
    form_class = ClienteForm

    def form_valid(self, form):
        response = super().form_valid(form)

        self.object.save()

        return response
    
class ClienteBorrar(View):
    print("llego aqui")
    def get(self, request, *args, **kwargs):
        cliente  = get_object_or_404(Cliente, pk=kwargs['pk'])
        cliente .delete()
        return redirect('cliente_app:listado_clientes')