# Generated by Django 4.1.1 on 2022-11-13 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0013_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=500, unique=True)),
                ('about_us', models.CharField(max_length=1000, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='productdetail',
            name='Manufacture',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='productdetail',
            name='Manufacture_address',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='productdetail',
            name='Return_exchange',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productdetail',
            name='Return_policy',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='productdetail',
            name='Sellers',
            field=models.ManyToManyField(to='ecomapp.seller'),
        ),
    ]