# Generated by Django 5.1 on 2024-08-15 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_rename_tilte_property_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='sku',
            field=models.IntegerField(default=9936, unique=True),
        ),
    ]
