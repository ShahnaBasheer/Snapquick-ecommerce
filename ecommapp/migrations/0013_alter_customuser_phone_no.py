# Generated by Django 4.1.3 on 2023-01-11 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0012_alter_customuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
