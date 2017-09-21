# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-21 02:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Capitulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('numero', models.PositiveIntegerField()),
                ('publicacao', models.DateField()),
                ('capa', models.ImageField(default='capitulo_capa/None/no-img.jpg', upload_to='capitulo_capa/')),
            ],
        ),
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('sinopse', models.TextField()),
                ('publicacao', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Em publicação'), ('F', 'Finalizado')], default='P', max_length=2)),
                ('visualizacao', models.IntegerField()),
                ('gostei', models.IntegerField()),
                ('capa', models.ImageField(default='obra_capa/None/no-img.jpg', upload_to='obra_capa/')),
                ('disponivel', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField()),
                ('imagem', models.ImageField(default='pagina/None/no-img.jpg', upload_to='pagina/')),
                ('capitulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paginas', to='core.Capitulo')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resumo', models.TextField()),
                ('born', models.DateField(blank=True, null=True)),
                ('cidade', models.CharField(default='Não Informado', max_length=128)),
                ('pais', models.CharField(default='Não Informado', max_length=128)),
                ('foto_perfil', models.ImageField(blank=True, default='foto_perfil/None/no-img.jpg', null=True, upload_to='foto_perfil/')),
                ('seguindo', models.ManyToManyField(blank=True, related_name='seguidores', to='core.Perfil')),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='pagina',
            name='criado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paginas_criadas', to='core.Perfil'),
        ),
        migrations.AddField(
            model_name='obra',
            name='perfil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='obras', to='core.Perfil'),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='criado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='capitulos_criados', to='core.Perfil'),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='obra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='capitulos', to='core.Obra'),
        ),
    ]
