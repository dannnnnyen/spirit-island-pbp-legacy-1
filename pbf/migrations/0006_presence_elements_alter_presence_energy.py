# Generated by Django 4.0.1 on 2022-02-15 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbf', '0005_gameplayer_gained_this_turn_presence_energy'),
    ]

    operations = [
        migrations.AddField(
            model_name='presence',
            name='elements',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='presence',
            name='energy',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
