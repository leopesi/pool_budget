# Generated by Django 3.0.3 on 2020-06-04 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dimensoes', '0012_auto_20200603_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dimensaomodel',
            name='profundidade_media',
        ),
    ]
