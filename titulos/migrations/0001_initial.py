# Generated by Django 5.0.8 on 2024-08-27 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoAtividade',
            fields=[
                ('codigo', models.AutoField(help_text='Código do Titulo', primary_key=True, serialize=False)),
                ('descricao', models.CharField(help_text='Informe a descrição do Titulo', max_length=70)),
                ('nome', models.CharField(max_length=70, null=True)),
            ],
        ),
    ]
