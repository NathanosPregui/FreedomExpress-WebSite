# Generated by Django 4.2.11 on 2024-04-11 01:06

import Produtos.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Produtos', '0003_alter_produto_estoque'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='Produto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Produto', to='Produtos.produto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produto',
            name='distribuidor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Usuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ProdutosImagens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=Produtos.models.user_directory_path)),
                ('Produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProdutoImagens', to='Produtos.produto')),
            ],
        ),
    ]