# Generated by Django 5.0.4 on 2024-04-27 17:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.CharField(max_length=150)),
                ('sobrenome', models.CharField(max_length=150)),
                ('nome_empresa', models.CharField(max_length=100)),
                ('email_pessoal', models.EmailField(max_length=254)),
                ('email_empresa', models.EmailField(max_length=254)),
                ('stored_password', models.CharField(blank=True, max_length=8, null=True)),
                ('telefone', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
