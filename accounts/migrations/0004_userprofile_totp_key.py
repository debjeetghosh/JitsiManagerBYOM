# Generated by Django 2.2.6 on 2020-04-22 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200422_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='totp_key',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
