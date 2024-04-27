from django.contrib import admin
from usuarios.models import Perfil
import random
import string

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_last_name', 'user_email', 'nome_empresa', 'email_empresa', 'telefone', 'generate_password']
    search_fields = ['user', 'user__username', 'user__last_name', 'user__email', 'nome_empresa', 'email_empresa', 'telefone']
    readonly_fields = ['stored_password']  

    def user_last_name(self, obj):
        return obj.user.last_name

    def user_email(self, obj):
        return obj.user.email

    def generate_password(self, obj):
        # Verifica se a senha já foi gerada e armazenada anteriormente
        if obj.stored_password:
            return obj.stored_password
        else:
            # Gera a senha aleatória
            random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            # Armazena a senha gerada no objeto
            obj.stored_password = random_password
            # Salva o objeto para persistir a senha no banco de dados
            obj.save()
            return random_password

    generate_password.short_description = 'Senha Gerada'




