# Generated by Django 3.0.3 on 2020-06-11 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dimensoes', '0017_auto_20200611_1859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientemodel',
            old_name='numerocasa',
            new_name='numero_casa',
        ),
        migrations.AddField(
            model_name='dimensaomodel',
            name='status',
            field=models.CharField(blank=True, choices=[('Em negociação', 'Em negociação'), ('Contrato', 'Contrato'), ('Encerrado', 'Encerrado')], default='Em negociação', help_text='Status do Orçamento', max_length=15),
        ),
    ]
