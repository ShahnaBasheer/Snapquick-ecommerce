# Generated by Django 4.1.1 on 2022-11-13 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0011_boysfashion_dlvry_charges_boysfashion_mrp_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boysfashion',
            old_name='seller',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='cartitem',
            old_name='seller',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='girlsfashion',
            old_name='seller',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='menfashion',
            old_name='seller',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='womenfashion',
            old_name='seller',
            new_name='brand',
        ),
    ]
