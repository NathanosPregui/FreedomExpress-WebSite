# Generated by Django 4.2.11 on 2024-04-08 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0002_rename_e_mail_usuario_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='complemento',
            field=models.CharField(max_length=80, null=True),
        ),
    ]