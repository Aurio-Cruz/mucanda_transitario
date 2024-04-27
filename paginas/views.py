from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect


from .forms import PaginaForm  # Importando o formulário PaginaForm 

class IndexView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy("login")
    template_name = "paginas/index.html"

    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Verificar o nome do usuário atual
        nome_usuario = self.request.user.username
        
        # Definir permissões com base no nome do usuário
        if nome_usuario == 'aurio':
            context['pertence_grupo_viaturas'] = True
        else:
            context['pertence_grupo_viaturas'] = False

        if nome_usuario == 'luciel':
            context['pertence_grupo_electronicos'] = True
        else:
            context['pertence_grupo_electronicos'] = False
        
        # Adicione verificações para outros usuários conforme necessário
        
        return context 

class SubmitPaginaView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy("login")
    template_name = "paginas/submit_pagina.html"

    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)   
    
    def post(self, request):
        form = PaginaForm(request.POST, request.FILES)
        if form.is_valid():
            form.send_email()
            return render(request, 'paginas/submit_pagina.html', {'success_message': True})  # Passa a variável success_message como True
        return render(request, 'paginas/submit_pagina.html', {'form': form})