# Generated by Django 4.1.1 on 2022-09-24 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boyscategory',
            name='boys',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='girlscategory',
            name='girls',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='mencategory',
            name='men',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='womencategory',
            name='women',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]