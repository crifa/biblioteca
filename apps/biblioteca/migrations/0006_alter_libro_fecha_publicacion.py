# Generated by Django 3.2.8 on 2022-05-17 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0005_auto_20220516_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='fecha_publicacion',
            field=models.DateField(blank=True, null=True),
        ),
    ]