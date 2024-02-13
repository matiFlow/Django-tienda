from django.shortcuts import render
from django.views.generic import TemplateView

############################ HOME VIEW ####################################

class Inicio(TemplateView):
    template_name = 'inicio.html'
    
