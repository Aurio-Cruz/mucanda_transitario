from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    primeiro_nome = models.CharField(max_length=150)  
    sobrenome = models.CharField(max_length=150) 
    nome_empresa = models.CharField(max_length=100)
    email_pessoal = models.EmailField()  
    email_empresa = models.EmailField()
    stored_password = models.CharField(max_length=8, blank=True, null=True)  
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username}'s Profile"