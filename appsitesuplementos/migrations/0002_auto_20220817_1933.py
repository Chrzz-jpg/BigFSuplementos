# Generated by Django 3.1.4 on 2022-08-17 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsitesuplementos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('descricao', models.CharField(max_length=300, verbose_name='descrição')),
            ],
        ),
        migrations.RenameModel(
            old_name='Produtos',
            new_name='Produto',
        ),
    ]