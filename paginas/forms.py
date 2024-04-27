from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class PaginaForm(forms.Form):
    usuario = forms.CharField(max_length=150, required=True)
    nome_produto = forms.CharField(max_length=100, required=True)
    descricao_produto = forms.CharField(widget=forms.Textarea, required=True)
    pais_origem = forms.CharField(max_length=100, required=True)
    quantidade = forms.IntegerField(required=True)
    imagem = forms.ImageField(required=True)

    def clean_usuario(self):
        username = self.cleaned_data.get('usuario')
        if not User.objects.filter(username=username).exists():
            raise ValidationError("Este usuário não está registrado.")
        return username
    
    PAISES = [
        "afeganistão", "albânia", "alemanha", "andorra", "angola",
        "antígua e barbuda", "arabia saudita", "argentina", "armenia", "austrália",
        "áustria", "azerbaijão", "bahamas", "bangladesh", "barbados",
        "barein", "bélgica", "belize", "benin", "bielorrússia",
        "bolívia", "bósnia e herzegovina", "botswana", "brasil", "brunei",
        "bulgária", "burkina faso", "burundi", "butão", "cabo verde",
        "camarões", "camboja", "canadá", "catar", "cazaquistão",
        "chade", "chile", "china", "chipre", "colômbia",
        "comores", "congo", "coréia do norte", "coréia do sul", "costa do marfim",
        "costa rica", "croácia", "cuba", "dinamarca", "djibouti",
        "dominica", "egito", "emirados árabes unidos", "equador", "eritreia",
        "eslováquia", "eslovênia", "espanha", "estados unidos", "estônia",
        "etiópia", "fiji", "filipinas", "finlândia", "frança",
        "gabão", "gâmbia", "geórgia", "gana", "grã-bretanha",
        "granada", "grécia", "guatemala", "guiana", "guiné",
        "guiné equatorial", "guiné-bissau", "haiti", "holanda", "honduras",
        "hungria", "iêmen", "índia", "indonésia", "irã",
        "iraque", "irlanda", "islândia", "israel", "itália",
        "jamaica", "japão", "jordânia", "kiribati", "kosovo",
        "kuwait", "laos", "lesoto", "letônia", "líbano",
        "libéria", "líbia", "liechtenstein", "lituânia", "luxemburgo",
        "macedônia", "madagascar", "malásia", "malaui", "maldivas",
        "mali", "malta", "marrocos", "maurícia", "mauritânia",
        "méxico", "mianmar", "micronésia", "moçambique", "moldávia",
        "mônaco", "mongólia", "montenegro", "namíbia", "nauru",
        "nepal", "nicarágua", "niger", "nigéria", "noruega",
        "nova zelândia", "omã", "palau", "palestina", "panamá",
        "papua nova guiné", "paquistão", "paraguai", "peru", "polônia",
        "portugal", "quirguistão", "quiribati", "reino unido", "república centro-africana",
        "república checa", "república democrática do congo", "república dominicana", "romênia", "ruanda",
        "rússia", "salomão", "samoa", "santa lúcia", "são cristóvão e névis",
        "são marino", "são tomé e príncipe", "são vicente e granadinas", "seicheles", "senegal",
        "serra leoa", "sérvia", "singapura", "síria", "somália",
        "sri lanka", "suazilândia", "sudão", "sudão do sul", "suécia",
        "suíça", "suriname", "tadjiquistão", "tailândia", "taiwan",
        "tanzânia", "timor leste", "togo", "tonga", "trinidad e tobago",
        "tunísia", "turcomenistão", "turquia", "tuvalu", "ucrânia",
        "uganda", "uruguai", "uzbequistão", "vanuatu", "vaticano",
        "venezuela", "vietnã", "zâmbia", "zimbábue",
    ]

    def clean_pais_origem(self):
        pais_origem = self.cleaned_data.get('pais_origem')
        if pais_origem.lower() not in [pais.lower() for pais in self.PAISES]:
            raise ValidationError("País de origem inválido ou verifica à acentuação")
        return pais_origem
    
    def clean_imagem(self):
        imagem = self.cleaned_data.get('imagem')
        if not imagem:
            raise ValidationError("Por favor, selecione uma imagem.")
        return imagem

    def send_email(self):
        usuario = self.cleaned_data['usuario']
        nome_produto = self.cleaned_data['nome_produto']
        descricao_produto = self.cleaned_data['descricao_produto']
        pais_origem = self.cleaned_data['pais_origem']
        quantidade = self.cleaned_data['quantidade']
        imagem = self.cleaned_data['imagem']

        # Construa o contexto para o template de email
        context = {
            'usuario': usuario,
            'nome_produto': nome_produto,
            'descricao_produto': descricao_produto,
            'pais_origem': pais_origem,
            'quantidade': quantidade,
        }

        # Renderize o template de email para texto simples
        email_content = render_to_string('paginas/email_template.html', context)
        text_content = strip_tags(email_content)

        # Envie o email
        email = EmailMultiAlternatives(
            'Novo Produto Submetido',
            text_content,  # Conteúdo do email em texto simples
            settings.EMAIL_HOST_USER,  # Seu email de envio
            ['aurionascimento142@gmail.com']  # Email específico para receber os dados
        )
        email.attach_alternative(email_content, "text/html")  # Conteúdo HTML do email
        email.attach(imagem.name, imagem.read(), imagem.content_type)  # Anexando a imagem
        email.send()
