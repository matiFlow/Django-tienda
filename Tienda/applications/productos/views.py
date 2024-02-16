from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Marca, Producto
from .form import MarcaForm, ProductoForm
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
class ProductoListar(ListView, LoginRequiredMixin):  #Listado de Productos
    model = Producto
    template_name = 'producto\listado.html'
    context_object_name = "lista"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        searchByTipo = self.request.GET.get("tipo")
        searchByDescripcion = self.request.GET.get("descripcion")
        searchByPrecioMinimo = self.request.GET.get("precioMinimo")
        searchByPrecioMaximo = self.request.GET.get("precioMaximo")

        if searchByTipo:
            queryset = queryset.filter(tipo__icontains=searchByTipo).distinct()
        
        if searchByDescripcion:
            queryset = queryset.filter(descripcion__icontains=searchByDescripcion).distinct()
        
        if searchByPrecioMinimo:
            queryset = queryset.filter(precio__gte = searchByPrecioMinimo).distinct()

        if searchByPrecioMaximo:
            queryset = queryset.filter(precio__lte = searchByPrecioMaximo).distinct()
        
        queryset = queryset.order_by('tipo')
            
        return queryset
    

class ProductoCrear(CreateView, LoginRequiredMixin): #Crear producto
    model = Producto
    template_name = 'producto\crear.html'
    form_class = ProductoForm
    success_url = reverse_lazy('producto_app:listado_productos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marca_form'] = MarcaForm()
        print("entro aqui") 
        return context

    def form_valid(self, form):
        producto = form.save(commit=False)
        producto.save()
        messages.success(self.request, 'Registro guardado con éxito')
        return super(ProductoCrear, self).form_valid(form)
    
    
class ProductoEditar(UpdateView, LoginRequiredMixin): #Crear producto
    model = Producto
    template_name = 'producto\editar.html'
    form_class = ProductoForm
    success_url = reverse_lazy('producto_app:listado_productos')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object 
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marca_form'] = MarcaForm()
        print("entro aqui") 
        return context

    def form_valid(self, form):
        producto = form.save(commit=False)
        producto.save()
        messages.success(self.request, 'Operacion realizada con éxito')
        return super(ProductoEditar, self).form_valid(form)
    
class ProductoBorrar(DeleteView, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        producto  = get_object_or_404(Producto, pk=kwargs['pk'])
        producto.delete()
        return redirect('producto_app:listado_productos')
    

class ProductoDetalles(DetailView, LoginRequiredMixin): 
    model = Producto
    template_name = "producto/detalle.html"
    context_object_name = "detalle"
    login_url = reverse_lazy('producto_app:listado_productos')


class MarcaCrear(CreateView, LoginRequiredMixin): #Crear marca
    model = Marca
    form_class = MarcaForm
    template_name = "producto/listado.html"
    
    def form_valid(self, form):
        print("entro aqui") 
        marca = form.save(commit=False)
        marca.save()
        response_data = {'success': True, 'message': 'Registro guardado con éxito'}
        return JsonResponse(response_data)
    
    def form_invalid(self, form):
        response_data = {'success': True, 'message': 'Errorm formuplario invalido'}
        return JsonResponse(response_data)