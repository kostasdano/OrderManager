# Generated by Django 2.2 on 2020-01-07 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
