from imaplib import _Authenticator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .serializer import ClienteSerializer
from .models import Cliente
from .form import ClienteForm, LoginForm
from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    DetailView
)
from django.views.generic.edit import (
    FormView
)
from rest_framework.generics import ListAPIView

@method_decorator(login_required, name='dispatch')

# Create your views here.
############################ VIEWS ####################################
class ClienteListar(ListView, LoginRequiredMixin):  #Listado de clientes
    model = Cliente
    template_name = 'cliente\listado.html'
    context_object_name = "lista"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
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
    

class ClienteCrear(CreateView, LoginRequiredMixin): #Crear cliente
    model = Cliente
    template_name = 'cliente\crear.html'
    form_class = ClienteForm
    success_url = reverse_lazy('cliente_app:listado_clientes')

    def form_valid(self, form):
        cliente = form.save(commit=False)
        cliente.save()
        messages.success(self.request, 'Registro guardado con éxito')
        return super(ClienteCrear, self).form_valid(form)
    
    
class ClienteEditar(UpdateView, LoginRequiredMixin): #Crear cliente
    model = Cliente
    template_name = 'cliente\editar.html'
    form_class = ClienteForm
    success_url = reverse_lazy('cliente_app:listado_clientes')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object 
        return kwargs

    def form_valid(self, form):
        cliente = form.save(commit=False)
        cliente.save()
        messages.success(self.request, 'Operacion realizada con éxito')
        return super(ClienteEditar, self).form_valid(form)
    
class ClienteBorrar(DeleteView, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        cliente  = get_object_or_404(Cliente, pk=kwargs['pk'])
        cliente .delete()
        messages.success(self.request, 'Se elimino correctamente')
        return redirect('cliente_app:listado_clientes')
    

class ClienteDetalles(DetailView, LoginRequiredMixin): 
    model = Cliente
    template_name = "cliente/detalle.html"
    context_object_name = "detalle"
    login_url = reverse_lazy('inicio_app:login_user')


class LoginUser(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('inicio_app:inicio')
    context_object_name = 'login'
    
    def form_valid(self, form):
        user = _Authenticator(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
            )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)
    
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse_lazy(
                'inicio_app:login-user'
            )
        )

# APIS VIEW
    
class ClienteListApiView(ListAPIView):

    serializer_class = ClienteSerializer
    template_name = "cliente/listadoApi.html"

    def get_queryset(self):
        return Cliente.objects.all()