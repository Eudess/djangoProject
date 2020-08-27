# Generated by Django 3.0.7 on 2020-08-10 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='E-mail')),
                ('password', models.CharField(max_length=100, verbose_name='Password')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('sobrenome', models.CharField(blank=True, max_length=100, verbose_name='Sobrenome')),
                ('is_active', models.BooleanField(blank=True, default=True, verbose_name='Está Ativo?')),
                ('is_trusty', models.BooleanField(default=False, verbose_name='Email Confirmado?')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]