# Generated by Django 2.2.6 on 2020-04-17 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_auto_20200417_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='end_time',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='start_time',
            field=models.BigIntegerField(default=0),
        ),
    ]
