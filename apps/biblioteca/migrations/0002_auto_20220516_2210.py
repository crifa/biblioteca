# Generated by Django 3.2.8 on 2022-05-17 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='categorias',
            new_name='categoria',
        ),
        migrations.RemoveField(
            model_name='autor',
            name='apellido',
        ),
    ]