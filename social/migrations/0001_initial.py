# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-21 02:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.CharField(max_length=1024)),
                ('publicacao', models.DateTimeField()),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=1024)),
                ('envio', models.DateTimeField()),
                ('visualizada', models.BooleanField(default=False)),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensagens_recebidas', to='core.Perfil')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensagens_enviadas', to='core.Perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.CharField(max_length=1024)),
                ('imagem', models.ImageField(blank=True, default='postagem/None/no-img.jpg', null=True, upload_to='postagem/')),
                ('publicacao', models.DateTimeField()),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postagens', to='core.Perfil')),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='postagem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='social.Postagem'),
        ),
    ]
