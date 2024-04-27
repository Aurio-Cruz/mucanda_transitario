from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UsuarioForm
from django.views.generic import TemplateView

class UsuarioCreate(CreateView):
    template_name = "usuarios/adesao.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('sucesso')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

class SuccessView(TemplateView):
    template_name = "usuarios/tela_sucesso.html"
    

