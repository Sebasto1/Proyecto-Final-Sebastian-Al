# Generated by Django 4.0.5 on 2022-07-05 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ConsoApp', '0004_rename_ingreso_distribuidores_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='distribuidores',
            old_name='stock',
            new_name='ingreso',
        ),
    ]
