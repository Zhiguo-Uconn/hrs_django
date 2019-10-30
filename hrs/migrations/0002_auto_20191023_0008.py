# Generated by Django 2.2.6 on 2019-10-23 04:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hrs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='birthday',
            field=models.DateField(default='1970-01-01', verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='doc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Doctor'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='firstName',
            field=models.CharField(max_length=30, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='lastName',
            field=models.CharField(max_length=50, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='race',
            field=models.CharField(choices=[('W', 'White'), ('B', 'Black'), ('A', 'Asian'), ('H', 'Hispanic'), ('I', 'AI/AN')], max_length=1, verbose_name='Race'),
        ),
        migrations.CreateModel(
            name='MedRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a1c', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='A1c')),
                ('fastGlucose', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Fast Glucose')),
                ('recordTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrs.Patient', verbose_name='Patient')),
            ],
        ),
    ]