# Generated by Django 2.2.5 on 2019-09-25 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infodev', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='communicationdevice',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Активность'),
        ),
        migrations.AlterField(
            model_name='communicationdevice',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='communicationdevice',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Долгота'),
        ),
    ]
