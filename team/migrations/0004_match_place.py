# Generated by Django 4.0.6 on 2022-08-17 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_player_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='place',
            field=models.CharField(blank=True, choices=[('huba', 'Pod Hubą'), ('sulechowska', 'Sulechowska')], default='huba', max_length=30, null=True),
        ),
    ]
