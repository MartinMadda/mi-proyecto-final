# Generated by Django 4.1.2 on 2022-10-21 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_configuracion_construido_por_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='subtitulo_principal',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='configuracion',
            name='titulo_principal',
            field=models.CharField(default='', max_length=30),
        ),
    ]
