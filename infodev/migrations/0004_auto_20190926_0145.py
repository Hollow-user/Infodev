# Generated by Django 2.2.5 on 2019-09-25 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infodev', '0003_auto_20190925_1739'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='communicationdevice',
            options={'ordering': ['id'], 'verbose_name': 'Устройство', 'verbose_name_plural': 'Устройства'},
        ),
    ]