# Generated by Django 2.0.7 on 2018-07-14 04:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hmc_number', models.IntegerField(default=1)),
                ('shift', models.FloatField(default=1)),
                ('diesel_start_percentage', models.FloatField(default=100)),
                ('diesel_end_percentage', models.FloatField(default=0)),
                ('diesel_start_hours', models.FloatField(default=0)),
                ('diesel_end_hours', models.FloatField(default=0)),
                ('total_tonnage_or_boxes', models.FloatField(default=0)),
                ('cycles', models.FloatField(default=0)),
                ('shift_end_flag', models.IntegerField(default=0)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_slot_start', models.TimeField(verbose_name='Time of start')),
                ('time_slot_stop', models.TimeField(verbose_name='Time of stop')),
                ('reason', models.CharField(default='NO', max_length=10)),
                ('remark', models.CharField(default='Nothing', max_length=200)),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Shift')),
            ],
        ),
        migrations.CreateModel(
            name='Vessel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vessel_name', models.CharField(default='None', max_length=100)),
                ('vessel_cargo', models.CharField(default='None', max_length=100)),
                ('berth_number', models.IntegerField(default=1)),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Slot')),
            ],
        ),
    ]