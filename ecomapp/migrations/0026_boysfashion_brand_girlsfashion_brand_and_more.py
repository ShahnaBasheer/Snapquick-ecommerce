# Generated by Django 4.1.1 on 2022-11-15 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0025_remove_boysfashion_brand_remove_girlsfashion_brand_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='boysfashion',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecomapp.brand'),
        ),
        migrations.AddField(
            model_name='girlsfashion',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecomapp.brand'),
        ),
        migrations.AddField(
            model_name='menfashion',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecomapp.brand'),
        ),
        migrations.AddField(
            model_name='womenfashion',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecomapp.brand'),
        ),
    ]
