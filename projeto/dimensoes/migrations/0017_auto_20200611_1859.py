# Generated by Django 3.0.3 on 2020-06-11 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dimensoes', '0016_auto_20200611_1852'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientemodel',
            old_name='numero_casa',
            new_name='numerocasa',
        ),
    ]