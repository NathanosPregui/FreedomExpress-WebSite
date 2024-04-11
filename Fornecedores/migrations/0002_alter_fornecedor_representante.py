# Generated by Django 4.2.11 on 2024-04-10 22:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Fornecedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='representante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='representantes', to=settings.AUTH_USER_MODEL),
        ),
    ]
