# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-14 06:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0004_auto_20160813_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_transaksi_peminjaman',
            name='nama_peminjam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='karyawan.biodata_karyawan'),
        ),
    ]