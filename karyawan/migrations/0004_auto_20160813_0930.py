# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-13 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0003_izin_karyawan_kehadiran_karyawan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kehadiran_karyawan',
            name='jenis_kehadiran',
            field=models.CharField(choices=[('cuti', 'Cuti'), ('hadir', 'Hadir'), ('izin', 'Izin'), ('alpa', 'Tanpa Kehadiran')], max_length=50),
        ),
    ]
