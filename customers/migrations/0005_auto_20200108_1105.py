# Generated by Django 2.2 on 2020-01-08 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
