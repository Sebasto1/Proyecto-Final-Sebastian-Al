# Generated by Django 4.0.4 on 2022-06-27 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConsoApp', '0002_alter_consolas_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consolas',
            name='stock',
            field=models.IntegerField(),
        ),
    ]
