# Generated by Django 4.2.5 on 2023-09-06 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_log_name_alter_round_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='name',
            field=models.CharField(blank=True, max_length=55),
        ),
        migrations.AlterField(
            model_name='round',
            name='player',
            field=models.CharField(blank=True, max_length=55),
        ),
    ]
