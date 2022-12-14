# Generated by Django 4.0.6 on 2022-10-20 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0006_sms_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sms',
            name='phone_numbers',
            field=models.TextField(blank=True, null=True, verbose_name='Numery adresatów'),
        ),
        migrations.AlterField(
            model_name='sms',
            name='request',
            field=models.TextField(blank=True, null=True, verbose_name='request'),
        ),
        migrations.AlterField(
            model_name='sms',
            name='response',
            field=models.TextField(blank=True, null=True, verbose_name='response'),
        ),
        migrations.CreateModel(
            name='TrainingDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_day', models.IntegerField(verbose_name='Dzień tygodnia')),
                ('hour', models.IntegerField(verbose_name='Godzina')),
                ('player', models.ManyToManyField(to='team.player')),
            ],
        ),
    ]
