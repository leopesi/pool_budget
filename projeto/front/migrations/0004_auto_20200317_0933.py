# Generated by Django 3.0.3 on 2020-03-17 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0003_remove_dimensaomodel_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dimensaomodel',
            name='construcao',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='dimensaomodel',
            name='contra_piso',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='dimensaomodel',
            name='escavacao',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='dimensaomodel',
            name='instalacao_vinil',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='dimensaomodel',
            name='remocao_terra',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
