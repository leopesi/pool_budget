# Generated by Django 3.0.3 on 2020-03-16 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=30)),
                ('cidade', models.CharField(blank=True, max_length=20)),
                ('estado', models.CharField(blank=True, max_length=15)),
                ('rua', models.CharField(blank=True, max_length=100)),
                ('numero_casa', models.CharField(blank=True, max_length=6)),
                ('cep', models.CharField(blank=True, max_length=20)),
                ('telefone', models.CharField(blank=True, max_length=15)),
                ('email', models.EmailField(blank=True, help_text='Ex. clinte@gmail.com', max_length=50)),
            ],
            options={
                'ordering': ['nome', 'sobrenome'],
            },
        ),
        migrations.CreateModel(
            name='DimensaoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comprimento', models.FloatField(help_text='Ex. 8.00', max_length=3)),
                ('largura', models.FloatField(help_text='Ex. 4.00', max_length=3)),
                ('prof_inicial', models.FloatField(help_text='Ex. 1.20', max_length=3)),
                ('prof_final', models.FloatField(help_text='Ex. 1.40', max_length=3)),
                ('largura_calcada', models.FloatField(blank=True, default=1, help_text='Ex. 1.00', max_length=3)),
                ('espessura', models.CharField(choices=[['0.6', '0.6 mm'], ['0.7', '0.7 mm'], ['0.8', '0.8 mm']], help_text='Espessura do vinil', max_length=3)),
                ('fornecedor', models.CharField(choices=[['sodramar', 'Sodramar'], ['viniplas', 'Viniplas']], help_text='Fornecedor do vinil', max_length=8)),
                ('profundidade_media', models.FloatField(max_length=5)),
                ('area_calcada', models.FloatField(max_length=5)),
                ('perimetro', models.FloatField(max_length=5)),
                ('m2_facial', models.FloatField(max_length=5)),
                ('m2_parede', models.FloatField(max_length=5)),
                ('m2_total', models.FloatField(max_length=5)),
                ('m3_total', models.FloatField(max_length=5)),
                ('m3_real', models.FloatField(max_length=5)),
                ('filtro', models.CharField(max_length=30)),
                ('motobomba', models.CharField(max_length=30)),
                ('tampa_casa_maquinas', models.CharField(max_length=30)),
                ('sacos_areia', models.CharField(max_length=30)),
                ('vinil_m2', models.FloatField(max_length=5)),
                ('isomanta_m2', models.FloatField(max_length=5)),
                ('perfil_fixo_m', models.FloatField(max_length=5)),
                ('escavacao', models.CharField(max_length=30)),
                ('construcao', models.CharField(max_length=30)),
                ('contra_piso', models.CharField(max_length=30)),
                ('remocao_terra', models.CharField(max_length=30)),
                ('instalacao_vinil', models.CharField(max_length=30)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(blank=True, choices=[('Em negociação', 'Em negociação'), ('Contrato', 'Contrato'), ('Encerrado', 'Encerrado')], default='Em negociação', help_text='Status do Orçamento', max_length=15)),
            ],
        ),
    ]
