# Generated by Django 4.1.1 on 2022-11-28 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0040_kidscategory_kidsfashion_kidsdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kidsfashion',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.kidscategory'),
        ),
    ]
