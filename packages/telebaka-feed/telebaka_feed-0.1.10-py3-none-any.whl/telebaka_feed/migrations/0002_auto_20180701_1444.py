# Generated by Django 2.0.5 on 2018-07-01 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telebaka_feed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vkfeed',
            name='bot',
            field=models.ForeignKey(limit_choices_to={'plugin_name': 'telebaka_feed'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bots.TelegramBot'),
        ),
    ]
