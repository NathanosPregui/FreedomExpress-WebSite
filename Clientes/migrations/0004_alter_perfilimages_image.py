# Generated by Django 4.2.11 on 2024-04-10 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0003_remove_perfilimages_caption_perfilimages_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/%y'),
        ),
    ]
