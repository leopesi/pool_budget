# Generated by Django 3.0.3 on 2020-06-18 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dimensoes', '0018_auto_20200611_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientemodel',
            name='numero_casa',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
