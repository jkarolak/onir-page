# Generated by Django 4.0.6 on 2022-09-01 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_sms'),
    ]

    operations = [
        migrations.AddField(
            model_name='sms',
            name='sent',
            field=models.BooleanField(default=False),
        ),
    ]