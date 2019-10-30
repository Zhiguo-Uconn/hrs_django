# Generated by Django 2.2.6 on 2019-10-28 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrs', '0005_auto_20191028_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medrecord',
            name='MaritalStatus',
            field=models.CharField(choices=[('Audio', (('vinyl', 'Vinyl'), ('cd', 'CD'))), ('Video', (('vhs', 'VHS Tape'), ('dvd', 'DVD'))), ('unknown', 'Unknown')], max_length=50, verbose_name='Marital Status'),
        ),
    ]
